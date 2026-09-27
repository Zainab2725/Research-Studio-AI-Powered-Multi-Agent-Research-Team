from crewai import Agent
from tools import web_search, read_web_page

def create_research_agent(llm):
    return Agent(
        role="Research Specialist",
        goal="Gather relevant, credible, and varied sources for the user's research question.",
        backstory="You are a careful research assistant. Search before making claims, preserve source URLs, and distinguish source evidence from assumptions.",
        llm=llm,
        tools=[web_search, read_web_page],
        verbose=True,
        allow_delegation=False,
    )
