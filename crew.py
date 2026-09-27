from crewai import Crew, Process
from llm_config import get_llm
from agents.research_agent import create_research_agent
from agents.analysis_agent import create_analysis_agent
from agents.writer_agent import create_writer_agent
from agents.fact_checker_agent import create_fact_checker_agent
from tasks import create_tasks

def run_research(topic: str, depth: str = "Standard") -> str:
    llm = get_llm()
    research_agent = create_research_agent(llm)
    analysis_agent = create_analysis_agent(llm)
    writer_agent = create_writer_agent(llm)
    fact_checker_agent = create_fact_checker_agent(llm)

    tasks = create_tasks(
        topic, depth, research_agent, analysis_agent, writer_agent, fact_checker_agent
    )
    crew = Crew(
        agents=[research_agent, analysis_agent, writer_agent, fact_checker_agent],
        tasks=tasks,
        process=Process.sequential,
        verbose=True,
    )
    result = crew.kickoff()
    return str(result)
