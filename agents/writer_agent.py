from crewai import Agent

def create_writer_agent(llm):
    return Agent(
        role="Research Report Writer",
        goal="Write a clear, well-structured report based on the research and analysis provided.",
        backstory="You write accessible reports with an executive summary, key findings, limitations, and source links. Never fabricate citations.",
        llm=llm,
        tools=[],
        verbose=True,
        max_iter = 1,
        allow_delegation=False,
    )
