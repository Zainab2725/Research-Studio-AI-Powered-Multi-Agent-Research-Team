import os
import streamlit as st
from crewai import LLM
import crewai.llms.cache as crewai_cache

MODEL = "groq/openai/gpt-oss-20b"

# Disable CrewAI's cache_breakpoint injection.
# Groq does not accept this field.
crewai_cache.mark_cache_breakpoint = lambda msg: msg

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
        model="groq/openai/gpt-oss-20b",
        api_key=st.secrets["GROQ_API_KEY"],
        temperature=0.1,
        max_tokens=1000,
        reasoning_effort="low",
    )
