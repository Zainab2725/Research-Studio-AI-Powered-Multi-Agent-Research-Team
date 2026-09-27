from crewai import Crew, Process

from agents.research_agent import research_agent
from agents.writer_agent import writer_agent

from tasks import create_research_task, create_report_task


def create_crew(topic):

    research_task = create_research_task(topic)
    report_task = create_report_task(topic)

    crew = Crew(
        agents=[
            research_agent,
            writer_agent,
        ],

        tasks=[
            research_task,
            report_task,
        ],

        process=Process.sequential,

        verbose=True,
    )

    return crew
