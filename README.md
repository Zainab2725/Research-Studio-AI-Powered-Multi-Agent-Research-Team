# Research Agent Team

A modular multi-agent research application built with Streamlit, CrewAI, and Groq's GPT-OSS 20B model.

## Agents

1. **Research Specialist** — gathers web sources using Serper search and reads public pages.
2. **Research Analyst** — synthesizes evidence and uses a calculator tool for basic arithmetic.
3. **Research Report Writer** — creates a structured Markdown report.
4. **Evidence and Citation Auditor** — reviews important claims and produces an audited final report.

The workflow is sequential. The report is generated from the research gathered during the run; web sources and model output should still be independently reviewed for high-stakes use.

## Requirements

- Python 3.10–3.13 recommended; use Python 3.12 on Streamlit Community Cloud.
- Groq API key with access to `openai/gpt-oss-20b`.
- Serper API key for web search.

## Deploy to Streamlit Community Cloud

1. Upload this repository to GitHub.
2. Create an app at https://share.streamlit.io/
3. Select this repository, branch `main`, and main file `app.py`.
4. In app settings, add these secrets:

```toml
GROQ_API_KEY = "your-groq-api-key"
SERPER_API_KEY = "your-serper-api-key"
```

5. Select Python 3.12 if available and deploy.

## Local secrets format (optional)

If running locally, create `.streamlit/secrets.toml` with the same keys. Do not commit that file.

## Notes

- API usage may incur costs or be subject to provider rate limits.
- Serper has its own plan and usage limits.
- Never commit API keys to GitHub.
- Web page extraction may fail on sites that block automated requests or render content with JavaScript.
- This is an MVP; review generated claims and citations before relying on the report.
