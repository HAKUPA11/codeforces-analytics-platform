import streamlit as st
import plotly.express as px

from queries.submission_queries import (
    get_verdict_distribution,
    get_language_distribution,
    get_submission_timeline,
    get_recent_submissions
)

st.set_page_config(
    page_title="Submission Analytics",
    page_icon="📄",
    layout="wide"
)

st.title("Submission Analytics")

# -------------------------------
# Pie Chart
# -------------------------------

left, right = st.columns(2)

with left:

    verdict_df = get_verdict_distribution()

    fig = px.pie(
        verdict_df,
        names="verdict",
        values="total",
        title="Verdict Distribution"
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )

# -------------------------------
# Language Chart
# -------------------------------

with right:

    language_df = get_language_distribution()

    fig = px.bar(
        language_df,
        x="programming_language",
        y="total",
        title="Programming Language Distribution"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Language",
        yaxis_title="Submissions"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )

# -------------------------------
# Submission Timeline
# -------------------------------

timeline_df = get_submission_timeline()

fig = px.line(
    timeline_df,
    x="submission_date",
    y="total_submissions",
    markers=True,
    title="Submission Timeline"
)

fig.update_layout(
    template="plotly_white",
    hovermode="x unified"
)

st.plotly_chart(
    fig,
    use_container_width=True,
    config={"displayModeBar": False}
)

# -------------------------------
# Recent Submissions
# -------------------------------

st.subheader("Recent Submissions")

submission_df = get_recent_submissions()

st.dataframe(
    submission_df,
    use_container_width=True,
    hide_index=True
)