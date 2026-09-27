from crewai import Crew, Process

from agents.research_specialist import research_specialist
from agents.report_writer import report_writer

from tasks import create_research_task, create_report_task


def run_research(topic: str):
    """
    Run the complete two-agent research workflow.

    1. Research Specialist searches for reliable evidence.
    2. Report Writer turns that evidence into the final report.
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
