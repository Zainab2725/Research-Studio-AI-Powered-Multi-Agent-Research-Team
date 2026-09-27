from crewai import Agent
from tools import calculator

def create_analysis_agent(llm):
    return Agent(
        role="Research Analyst",
        goal="Analyze the gathered evidence, identify themes, disagreements, limitations, and useful quantitative comparisons.",
        backstory="You analyze evidence carefully. Do not invent facts. Use the calculator tool for arithmetic when needed.",
        llm=llm,
        tools=[calculator],
        verbose=True,
        allow_delegation=False,
    )
