import streamlit as st
import crewai.llms.cache as crewai_cache
from crewai import LLM


# Workaround for Groq cache_breakpoint compatibility
crewai_cache.mark_cache_breakpoint = lambda msg: msg


def get_llm():
    return LLM(
        model="groq/openai/gpt-oss-20b",
        api_key=st.secrets["GROQ_API_KEY"],
        temperature=0.1,
        max_tokens=450,
        reasoning_effort="low",
    )
