import streamlit as st
import crewai.llms.cache as crewai_cache
from crewai import LLM


# Prevent CrewAI from sending the unsupported cache_breakpoint
# field to Groq.
crewai_cache.mark_cache_breakpoint = lambda msg: msg


def get_llm():
    return LLM(
        model="groq/openai/gpt-oss-20b",
        api_key=st.secrets["GROQ_API_KEY"],
        temperature=0.1,
        max_tokens=600,
        reasoning_effort="low",
    )
