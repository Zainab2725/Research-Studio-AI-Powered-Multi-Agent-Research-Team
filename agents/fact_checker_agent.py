from crewai import Agent
from tools import web_search, read_web_page

def create_fact_checker_agent(llm):
    return Agent(
        role="Evidence and Citation Auditor",
        goal="Audit important claims in the draft against available source material and flag unsupported or overstated claims.",
        backstory="You are a skeptical fact-checker. Use tools to verify key claims where possible. Never claim a source was verified unless you inspected relevant evidence.",
        llm=llm,
        tools=[web_search, read_web_page],
        verbose=True,
        allow_delegation=False,
    )
