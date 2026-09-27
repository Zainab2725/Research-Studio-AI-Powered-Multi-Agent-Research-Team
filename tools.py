import os
from crewai.tools import tool
import requests
import streamlit as st

def _get_secret(name: str):
    """Read a secret from Streamlit Cloud, with an environment fallback."""
    try:
        value = st.secrets.get(name)
        if value:
            return value
    except Exception:
        pass
    return os.getenv(name)

@tool("Web Search")
def web_search(query: str) -> str:
    """Search the web for useful research sources using the Serper API."""
    api_key = _get_secret("SERPER_API_KEY")
    if not api_key:
        return "Web search unavailable: SERPER_API_KEY is missing."
    try:
        response = requests.post(
            "https://google.serper.dev/search",
            headers={"X-API-KEY": api_key, "Content-Type": "application/json"},
            json={"q": query, "num": 8},
            timeout=25,
        )
        response.raise_for_status()
        data = response.json()
        results = data.get("organic", [])
        if not results:
            return "No web results found."
        lines = []
        for i, item in enumerate(results, 1):
            lines.append(
                f"{i}. {item.get('title', 'Untitled')}\n"
                f"URL: {item.get('link', '')}\n"
                f"Snippet: {item.get('snippet', '')}"
            )
        return "\n\n".join(lines)
    except requests.RequestException as exc:
        return f"Web search error: {exc}"

@tool("Read Web Page")
def read_web_page(url: str) -> str:
    """Fetch and extract readable text from a public web page URL."""
    from bs4 import BeautifulSoup
    from urllib.parse import urlparse

    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        return "Invalid URL. Provide a public http or https URL."
    try:
        response = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0 (compatible; ResearchAgentTeam/1.0)"},
            timeout=20,
        )
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header", "noscript"]):
            tag.decompose()
        text = " ".join(soup.get_text(" ", strip=True).split())
        return text[:12000] if text else "No readable text extracted."
    except requests.RequestException as exc:
        return f"Page read error: {exc}"

@tool("Calculator")
def calculator(expression: str) -> str:
    """Evaluate a basic arithmetic expression. Only digits, spaces, decimal points, and arithmetic operators are accepted."""
    import ast
    import operator

    ops = {
        ast.Add: operator.add, ast.Sub: operator.sub,
        ast.Mult: operator.mul, ast.Div: operator.truediv,
        ast.Pow: operator.pow, ast.USub: operator.neg,
        ast.UAdd: operator.pos, ast.Mod: operator.mod,
    }

    def evaluate(node):
        if isinstance(node, ast.Expression):
            return evaluate(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in ops:
            return ops[type(node.op)](evaluate(node.left), evaluate(node.right))
        if isinstance(node, ast.UnaryOp) and type(node.op) in ops:
            return ops[type(node.op)](evaluate(node.operand))
        raise ValueError("Unsupported expression")

    try:
        if len(expression) > 100:
            return "Expression too long."
        tree = ast.parse(expression, mode="eval")
        return str(evaluate(tree))
    except Exception as exc:
        return f"Could not calculate expression: {exc}"
