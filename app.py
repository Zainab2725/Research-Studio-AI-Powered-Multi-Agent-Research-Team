import streamlit as st
from crew import run_research

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Research Studio",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');

    :root {
        --ink: #17152B;
        --muted: #74738A;
        --purple: #6D4AFF;
        --purple-dark: #5535D9;
        --line: #E9E7F2;
        --soft: #F7F5FF;
    }

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(
                circle at 88% 0%,
                rgba(109, 74, 255, .09),
                transparent 28rem
            ),
            #FBFAFE;
        color: var(--ink);
    }

    .block-container {
        max-width: 1240px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3 {
        font-family: 'Manrope', sans-serif !important;
        letter-spacing: -0.035em;
        color: var(--ink);
    }

    [data-testid="stSidebar"] {
        background: #F5F2FF;
        border-right: 1px solid #E8E2FF;
    }

    [data-testid="stSidebar"] .block-container {
        padding-top: 1.7rem;
    }

    .brand {
        font-family: 'Manrope', sans-serif;
        font-size: 1.25rem;
        font-weight: 800;
        letter-spacing: -0.04em;
        color: var(--ink);
    }

    .brand span {
        color: var(--purple);
    }

    .eyebrow {
        color: var(--purple);
        text-transform: uppercase;
        letter-spacing: .14em;
        font-size: .72rem;
        font-weight: 800;
        margin-bottom: .65rem;
    }

    .hero-title {
        font-family: 'Manrope', sans-serif;
        font-size: clamp(2.15rem, 4vw, 3.45rem);
        line-height: 1.08;
        letter-spacing: -.055em;
        font-weight: 800;
        color: var(--ink);
        margin: 0;
    }

    .hero-copy {
        color: var(--muted);
        font-size: 1.04rem;
        line-height: 1.7;
        max-width: 720px;
        margin-top: .9rem;
    }

    .panel {
        background: rgba(255, 255, 255, .92);
        border: 1px solid var(--line);
        border-radius: 20px;
        padding: 1.35rem;
        box-shadow: 0 8px 30px rgba(39, 25, 91, .035);
    }

    .metric-label {
        color: var(--muted);
        font-size: .78rem;
        font-weight: 700;
        letter-spacing: .06em;
    }

    .metric-value {
        color: var(--ink);
        font-family: 'Manrope', sans-serif;
        font-size: 1.35rem;
        font-weight: 800;
        margin-top: .3rem;
    }

    .step-number {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-width: 30px;
        height: 30px;
        border-radius: 9px;
        background: #EEE9FF;
        color: var(--purple-dark);
        font-weight: 800;
        font-size: .82rem;
    }

    .small-muted {
        color: var(--muted);
        font-size: .88rem;
        line-height: 1.6;
    }

    .stButton > button,
    .stDownloadButton > button,
    .stFormSubmitButton > button {
        border-radius: 11px;
        min-height: 2.8rem;
        font-weight: 700;
        transition: all .15s ease;
    }

    .stButton > button[kind="primary"],
    .stFormSubmitButton > button[kind="primary"] {
        background: var(--purple);
        color: white;
        border: 1px solid var(--purple);
        box-shadow: 0 7px 18px rgba(109, 74, 255, .18);
    }

    .stButton > button[kind="primary"]:hover,
    .stFormSubmitButton > button[kind="primary"]:hover {
        background: var(--purple-dark);
        border-color: var(--purple-dark);
        transform: translateY(-1px);
    }

    .stDownloadButton > button {
        background: white;
        color: var(--purple-dark);
        border: 1px solid #DCD4FF;
    }

    .stTextArea textarea {
        border-radius: 12px;
        background: #FFFFFF;
    }

    div[data-testid="stTabs"] button {
        font-weight: 700;
    }

    .status-pill {
        display: inline-block;
        background: #F0EBFF;
        color: #5535D9;
        padding: .35rem .7rem;
        border-radius: 999px;
        font-size: .78rem;
        font-weight: 700;
    }

    .footer-note {
        color: #9290A3;
        font-size: .78rem;
        text-align: center;
        padding-top: 2.5rem;
    }

    @media (max-width: 700px) {
        .block-container {
            padding: 1.1rem 1rem 2rem;
        }

        .panel {
            padding: 1rem;
            border-radius: 16px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# SESSION STATE
# =========================================================

if "research_result" not in st.session_state:
    st.session_state.research_result = None

if "research_topic" not in st.session_state:
    st.session_state.research_topic = ""

if "draft_topic" not in st.session_state:
    st.session_state.draft_topic = ""

if "draft_depth" not in st.session_state:
    st.session_state.draft_depth = "Standard"


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    st.markdown(
        '<div class="brand"><span>Research</span> Studio</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="small-muted" style="margin-top:.45rem">'
        'Your workspace for evidence-led research.'
        '</div>',
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("#### Research team")

    st.markdown(
        """
        <div class="small-muted">
        <b>04 specialist agents</b><br>
        Research → Analyze → Write → Audit
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("#### Model")

    st.markdown(
        """
        <div class="small-muted">
        <b>Groq GPT-OSS 20B</b><br>
        CrewAI sequential workflow
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("#### Research tips")

    st.markdown(
        """
        <div class="small-muted">
        • Specify your research question.<br><br>
        • Include a time period or location when relevant.<br><br>
        • Ask for comparisons, evidence, and limitations.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    if st.button("Clear current report", use_container_width=True):
        st.session_state.research_result = None
        st.session_state.research_topic = ""
        st.session_state.draft_topic = ""
        st.rerun()


# =========================================================
# HERO SECTION
# =========================================================

st.markdown(
    '<div class="eyebrow">Multi-agent research workspace</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="hero-title">Turn a question into<br>structured research.</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-copy">
    A coordinated team researches the web, analyzes evidence,
    drafts a report, and audits important claims — all in one
    streamlined workspace.
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

# =========================================================
# OVERVIEW METRICS
# =========================================================

m1, m2, m3 = st.columns(3)

metrics = [
    (m1, "SPECIALIST AGENTS", "04"),
    (m2, "WORKFLOW", "Sequential"),
    (m3, "LANGUAGE MODEL", "GPT-OSS 20B"),
]

for col, label, value in metrics:
    with col:
        st.markdown(
            f"""
            <div class="panel">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("")

# =========================================================
# MAIN WORKSPACE
# =========================================================

left, right = st.columns([1.4, 1], gap="large")

with left:
    st.markdown('<div class="panel">', unsafe_allow_html=True)

    st.markdown("### Start a research brief")

    st.markdown(
        '<div class="small-muted">'
        'Describe what you need. Your research team will use this brief '
        'to guide its work.'
        '</div>',
        unsafe_allow_html=True,
    )

    with st.form("research_form", clear_on_submit=False):
        topic = st.text_area(
            "Research question or topic",
            value=st.session_state.draft_topic,
            placeholder=(
                "Example: How are multi-agent AI systems being used "
                "in healthcare? Compare applications, benefits, risks, "
                "and open challenges."
            ),
            height=160,
            help="Specific questions usually produce more focused research.",
        )

        depth = st.select_slider(
            "Report length",
            options=["Concise", "Standard", "Detailed"],
            value=st.session_state.draft_depth,
        )

        submitted = st.form_submit_button(
            "Run research team",
            type="primary",
            use_container_width=True,
        )

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="panel">', unsafe_allow_html=True)

    st.markdown("### Your research pipeline")

    steps = [
        ("01", "Research", "Find sources and collect evidence"),
        ("02", "Analyze", "Identify patterns and limitations"),
        ("03", "Write", "Build a structured report"),
        ("04", "Audit", "Review claims and references"),
    ]

    for number, title, description in steps:
        st.markdown(
            f"""
            <div style="display:flex;gap:.8rem;align-items:flex-start;margin:1.15rem 0">
                <span class="step-number">{number}</span>
                <div>
                    <div style="font-weight:750;color:#17152B">{title}</div>
                    <div class="small-muted">{description}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div style="
            background:#F7F5FF;
            border:1px solid #EAE4FF;
            border-radius:12px;
            padding:.9rem;
            margin-top:1rem;
        ">
            <div style="font-weight:700;color:#5535D9;margin-bottom:.3rem">
                Research note
            </div>
            <div class="small-muted">
                AI-generated findings and source links should be reviewed,
                especially for high-stakes decisions.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# RUN RESEARCH
# =========================================================

if submitted:
    st.session_state.draft_topic = topic
    st.session_state.draft_depth = depth

    if not topic.strip():
        st.warning("Please enter a research question or topic.")
    else:
        try:
            with st.status(
                "Your research team is working...",
                expanded=True,
            ) as status:
                st.write("Research Agent is gathering sources.")
                st.write("Analysis Agent is synthesizing evidence.")
                st.write("Report Writer is drafting the report.")
                st.write("Fact-Checker is reviewing important claims.")

                result = run_research(topic.strip(), depth)

                st.session_state.research_result = str(result)
                st.session_state.research_topic = topic.strip()

                status.update(
                    label="Research run complete",
                    state="complete",
                    expanded=False,
                )

            st.success("Your research report is ready.")

        except Exception as exc:
            st.error(f"Research run failed: {exc}")

            st.info(
                "Check that GROQ_API_KEY and SERPER_API_KEY are "
                "configured in Streamlit Secrets. If the keys are "
                "correct, review the app logs for details."
            )


# =========================================================
# RESEARCH REPORT
# =========================================================

result = st.session_state.research_result

if result:
    st.write("")
    st.divider()

    st.markdown("## Research report")

    st.markdown(
        f"""
        <div class="small-muted" style="margin-top:-.4rem;margin-bottom:1rem">
            Topic: {st.session_state.research_topic}
        </div>
        """,
        unsafe_allow_html=True,
    )

    report_tab, sources_tab, export_tab = st.tabs(
        ["Report", "Source review", "Export"]
    )

    with report_tab:
        st.markdown(result)

    with sources_tab:
        st.markdown("### Review your sources")

        st.markdown(
            """
            Check the source links included in the report. Confirm that
            each source is relevant and supports the claim associated
            with it.
            """
        )

        st.info(
            "This MVP displays the audited report text. A structured "
            "source table can be added in a future version."
        )

    with export_tab:
        st.markdown("### Download your report")

        st.markdown(
            "Save your research as Markdown or plain text."
        )

        col1, col2 = st.columns(2)

        with col1:
            st.download_button(
                "Download Markdown",
                data=result,
                file_name="research_report.md",
                mime="text/markdown",
                use_container_width=True,
            )

        with col2:
            st.download_button(
                "Download text",
                data=result,
                file_name="research_report.txt",
                mime="text/plain",
                use_container_width=True,
            )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer-note">
        Research Studio · Built with Streamlit, CrewAI, and Groq
    </div>
    """,
    unsafe_allow_html=True,
)
