import streamlit as st
from crew import run_research

st.set_page_config(page_title="Research Agent Team", page_icon=None, layout="wide")

st.title("Research Agent Team")
st.caption("A multi-agent research workflow powered by CrewAI and Groq GPT-OSS 20B.")

with st.sidebar:
    st.subheader("Configuration")
    st.write("Add GROQ_API_KEY and SERPER_API_KEY in Streamlit Cloud → App settings → Secrets.")
    st.caption("Keep API keys out of GitHub and out of this app's source code.")

topic = st.text_area(
    "What would you like to research?",
    placeholder="e.g. Applications, benefits, risks, and recent developments of multi-agent AI in healthcare",
    height=130,
)
depth = st.selectbox("Report depth", ["Concise", "Standard", "Detailed"], index=1)
if st.button("Start research", type="primary", disabled=not topic.strip()):
    with st.spinner("Research agents are working. This can take a few minutes..."):
        try:
            result = run_research(topic.strip(), depth)
            st.session_state["research_result"] = result
            st.session_state["research_topic"] = topic.strip()
        except Exception as exc:
            st.error(f"Research failed: {exc}")
            st.info("Check your API keys, Groq limits, and Streamlit logs.")

if st.session_state.get("research_result"):
    st.divider()
    st.subheader("Research report")
    st.markdown(st.session_state["research_result"])
    st.download_button(
        "Download report (.md)",
        data=st.session_state["research_result"],
        file_name="research_report.md",
        mime="text/markdown",
    )
