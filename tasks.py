from crewai import Task

from agents.research_specialist import research_specialist
from agents.report_writer import report_writer


def create_report_task(topic, depth="Standard"):
    return Task(
        description=f"""
Research this topic:

{topic}

Use web search to find reliable evidence.

Rules:

- Perform only one search cycle.
- Find a maximum of 3 strong sources.
- Prefer primary research papers, universities,
  government sources, official institutions,
  and reputable organizations.
- Do not repeatedly search the same topic.
- Do not invent sources, URLs, statistics, or findings.
- Be concise.

For each source provide:

1. Source title
2. URL
3. Publication date if available
4. One short evidence summary
5. Important numerical finding if available

Return only the research evidence needed by the report writer.
""",
        expected_output=(
            "A concise research brief containing no more than "
            "3 reliable sources and their verified evidence."
        ),
        agent=research_specialist,
    )


def create_report_task(topic, depth="Standard"):
    depth_rules = {
        "Concise": "Keep the report around 300-400 words.",
        "Standard": "Keep the report around 450-600 words.",
        "Detailed": "Keep the report around 650-800 words.",
    }

    selected_length = depth_rules.get(
        depth,
        depth_rules["Standard"],
    )

    return Task(
        description=f"""
Write a research report about:

{topic}

The requested report length is:

{depth}

{selected_length}

Use ONLY the research evidence supplied by the Research Specialist.

Do not perform additional web searches.

Do not invent:

- statistics
- sources
- URLs
- study results
- publication dates
- conclusions

Your report must:

1. State the main findings.
2. Compare evidence where appropriate.
3. Clearly distinguish reported findings from interpretation.
4. Mention important limitations and uncertainty.
5. Avoid unsupported claims.
6. Include only sources actually provided by the Research Specialist.

Use this structure:

Title

Executive Summary

Key Findings

Evidence and Analysis

Limitations and Uncertainty

Conclusion

Sources
""",
        expected_output=(
            f"A factual research report with the requested {depth.lower()} "
            "length, using only the supplied research evidence."
        ),
        agent=report_writer,
    )
