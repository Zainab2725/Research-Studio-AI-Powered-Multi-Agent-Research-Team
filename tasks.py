from crewai import Task


def create_tasks(
    topic,
    depth,
    research_agent,
    analysis_agent,
    writer_agent,
    fact_checker_agent,
):
    # Keep reports reasonably small for the Groq free-tier TPM limit.
    length = {
        "Concise": "about 500-700 words",
        "Standard": "about 700-900 words",
        "Detailed": "about 900-1200 words",
    }.get(depth, "about 700-900 words")

    # =========================================================
    # 1. RESEARCH TASK
    # =========================================================

    research_task = Task(
        description=(
            f"Research this topic: {topic}\n\n"
            "Use web search to find the most relevant and reliable evidence.\n"
            "Find a maximum of 3 strong sources.\n"
            "Prefer primary research papers, official institutions, "
            "universities, government sources, and reputable organizations.\n\n"
            "For each source provide:\n"
            "- Source title\n"
            "- URL\n"
            "- Publication date if available\n"
            "- 1-3 sentence evidence summary\n"
            "- Important numerical findings if available\n\n"
            "Do not repeatedly search for the same topic.\n"
            "Do not invent sources, URLs, statistics, or findings.\n"
            "Be concise."
        ),
        expected_output=(
            "A concise research brief containing no more than 3 sources, "
            "their URLs, dates when available, key evidence, numerical "
            "findings, limitations, and important uncertainty."
        ),
        agent=research_agent,
    )

    # =========================================================
    # 2. ANALYSIS TASK
    # =========================================================

    analysis_task = Task(
        description=(
            f"Analyze the research brief for: {topic}\n\n"
            "Use ONLY the evidence provided by the Research Specialist.\n"
            "Do not perform additional web searches.\n"
            "Do not invent facts or sources.\n\n"
            "Identify:\n"
            "- Major findings\n"
            "- Areas of agreement\n"
            "- Areas of disagreement\n"
            "- Strength of the evidence\n"
            "- Important limitations\n"
            "- Uncertainty or missing information\n\n"
            "Clearly distinguish documented findings from interpretation.\n"
            "Keep the analysis concise."
        ),
        expected_output=(
            "A concise evidence-based analysis containing major findings, "
            "comparisons, evidence quality, limitations, uncertainty, "
            "and unanswered questions."
        ),
        agent=analysis_agent,
        context=[research_task],
    )

    # =========================================================
    # 3. REPORT WRITER TASK
    # =========================================================

    writing_task = Task(
        description=(
            f"Write a {length} research report about: {topic}\n\n"
            "Use ONLY the research brief and analysis supplied by the "
            "previous agents.\n"
            "Do not perform additional research.\n"
            "Do not invent facts, statistics, citations, or references.\n\n"
            "Use this structure:\n"
            "1. Title\n"
            "2. Report Date\n"
            "3. Executive Summary\n"
            "4. Scope\n"
            "5. Key Findings\n"
            "6. Analysis\n"
            "7. Limitations and Uncertainty\n"
            "8. Conclusion\n"
            "9. Sources\n\n"
            "The Sources section must contain only sources actually "
            "provided by the Research Specialist.\n"
            "Keep the writing factual and appropriately qualified."
        ),
        expected_output=(
            "A polished Markdown research report with a clear structure, "
            "evidence-based findings, appropriate caveats, and numbered "
            "source URLs."
        ),
        agent=writer_agent,
        context=[research_task, analysis_task],
    )

    # =========================================================
    # 4. EVIDENCE & CITATION AUDIT
    # =========================================================

    audit_task = Task(
        description=(
            f"Audit the draft research report about: {topic}\n\n"
            "Use ONLY the research brief, analysis, and draft report "
            "provided to you.\n"
            "Do NOT perform additional web searches.\n"
            "Do NOT invent replacement sources.\n\n"
            "Check the report for:\n"
            "- Unsupported factual claims\n"
            "- Incorrect or mismatched citations\n"
            "- Numerical claims not supported by the research brief\n"
            "- Missing uncertainty or important context\n"
            "- Overconfident wording\n"
            "- Sources that were not actually provided by the researcher\n\n"
            "Correct the report where necessary.\n"
            "If a claim cannot be supported by the supplied evidence, "
            "remove it or clearly label it as uncertain/unverified.\n\n"
            "Return ONLY the final corrected research report."
        ),
        expected_output=(
            "A final audited Markdown research report containing only "
            "supported claims, valid supplied sources, appropriate "
            "uncertainty, and clear citations."
        ),
        agent=fact_checker_agent,
        context=[research_task, analysis_task, writing_task],
    )

    return [
        research_task,
        analysis_task,
        writing_task,
        audit_task,
    ]
