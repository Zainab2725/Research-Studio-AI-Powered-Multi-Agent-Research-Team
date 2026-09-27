from crewai import Crew, Process

from agents.research_specialist import research_specialist
from agents.report_writer import report_writer

from tasks import create_research_task, create_report_task


def run_research(topic: str):
    """
    Runs the complete research workflow.

    Research Specialist:
    - Searches the web
    - Finds reliable sources
    - Extracts evidence

    Report Writer:
    - Uses the research evidence
    - Produces the final report
    """

    research_task = create_research_task(topic)
    report_task = create_report_task(topic)

    crew = Crew(
        agents=[
            research_specialist,
            report_writer,
        ],
        tasks=[
            research_task,
            report_task,
        ],
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff()

    return result
