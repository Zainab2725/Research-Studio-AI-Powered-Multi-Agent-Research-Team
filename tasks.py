from crewai import Task

def create_tasks(topic, depth, research_agent, analysis_agent, writer_agent, fact_checker_agent):
    length = {
        "Concise": "about 700-1000 words",
        "Standard": "about 1200-1800 words",
        "Detailed": "about 2000-2800 words",
    }.get(depth, "about 1200-1800 words")

    research_task = Task(
        description=(
            f"Research this topic: {topic}\n"
            "Use web search to gather several relevant sources. Include source titles, URLs, snippets or extracted evidence. "
            "Prioritize primary sources and reputable institutions when available. Note dates and uncertainty. "
            "Do not invent sources."
        ),
        expected_output="A research brief containing findings, evidence, source titles, URLs, dates when available, and open questions.",
        agent=research_agent,
    )
    analysis_task = Task(
        description=(
            f"Analyze the research brief for: {topic}\n"
            "Identify major themes, areas of agreement and disagreement, evidence quality, limitations, and unanswered questions. "
            "Separate facts from interpretations. Use the calculator if a simple calculation is useful."
        ),
        expected_output="An evidence-led analysis with themes, comparisons, caveats, and gaps.",
        agent=analysis_agent,
        context=[research_task],
    )
    writing_task = Task(
        description=(
            f"Write a {length} research report on: {topic}\n"
            "Include: title, date of report, executive summary, scope, key findings, analysis, limitations, conclusion, and a numbered list of sources with URLs. "
            "Use only sources supplied in the research brief; do not fabricate references."
        ),
        expected_output="A polished Markdown research report with source URLs.",
        agent=writer_agent,
        context=[research_task, analysis_task],
    )
    audit_task = Task(
        description=(
            f"Audit the draft report about: {topic}\n"
            "Check the most important factual claims against the research brief and use search/page-reading tools for important claims where practical. "
            "Flag unsupported claims, mismatched citations, missing context, and overconfident wording. "
            "Return the corrected final report, preserving useful structure. If a claim cannot be verified, label it as unverified or qualify it."
        ),
        expected_output="A final audited Markdown report with source URLs and appropriate caveats.",
        agent=fact_checker_agent,
        context=[research_task, analysis_task, writing_task],
    )
    return [research_task, analysis_task, writing_task, audit_task]
