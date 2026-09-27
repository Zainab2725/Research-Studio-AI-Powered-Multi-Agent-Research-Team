from crewai import Task

from agents.research_specialist import research_specialist
from agents.report_writer import report_writer


def create_research_task(topic: str):
    return Task(
        description=f"""
Research the following question:

{topic}

Use the available web search tool.

Research rules:

- Perform only one focused search cycle.
- Find a maximum of 3 reliable sources.
- Prefer primary research, universities, government sources,
  official institutions, and reputable organizations.
- Do not repeatedly search the same topic.
- Do not invent sources, URLs, statistics, dates, or findings.
- Extract only evidence that directly helps answer the question.

For every source provide:

1. Source title
2. URL
3. Publication date if available
4. Short evidence summary
5. Important numerical finding, if available

Return a concise research brief for the Report Writer.
""",
        expected_output="""
A concise research brief containing:

- The main findings
- Maximum 3 sources
- Source titles
- URLs
- Publication dates when available
- Evidence summaries
- Important numerical findings when verified

No invented information.
""",
        agent=research_specialist,
    )


def create_report_task(topic: str, depth: str = "Standard"):
    length_rules = {
        "Concise": "Write approximately 300-400 words.",
        "Standard": "Write approximately 450-600 words.",
        "Detailed": "Write approximately 650-800 words.",
    }

    selected_length = length_rules.get(
        depth,
        length_rules["Standard"],
    )

    return Task(
        description=f"""
Write a research report answering:

{topic}

Requested report length:

{depth}

{selected_length}

IMPORTANT:

Use ONLY the research evidence provided by the
Research Specialist.

Do NOT perform additional web searches.

Do NOT invent:

- statistics
- sources
- URLs
- study results
- publication dates
- quotations
- conclusions

The report should:

1. Clearly answer the research question.
2. Present the main findings.
3. Compare evidence where appropriate.
4. Distinguish documented findings from interpretation.
5. Explain important limitations and uncertainty.
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
        expected_output=f"""
A factual {depth.lower()} research report that:

- Directly answers the research question
- Uses only supplied research evidence
- Contains no invented sources or statistics
- Includes limitations and uncertainty
- Includes a Sources section
- Is approximately the requested length
""",
        agent=report_writer,
    )
