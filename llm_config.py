import os
import streamlit as st
from crewai import LLM

MODEL = "groq/openai/gpt-oss-20b"

def get_secret(name: str):
    """Read a secret from Streamlit Cloud, with an environment fallback."""
    try:
        value = st.secrets.get(name)
        if value:
            return value
    except Exception:
        pass
    return os.getenv(name)

def get_llm():
    api_key = get_secret("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("Missing GROQ_API_KEY. Add it to Streamlit Cloud Secrets.")
    return LLM(
        model=MODEL,
        api_key=api_key,
        temperature=0.2,
    )
