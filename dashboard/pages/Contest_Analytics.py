import streamlit as st
import plotly.express as px

from queries.contest_queries import *

st.set_page_config(
    page_title="Contest Analytics",
    page_icon="🏆",
    layout="wide"
)

st.title("Contest Analytics")

left, right = st.columns(2)

with left:

    df = get_contest_type_distribution()

    fig = px.pie(
        df,
        names="contest_type",
        values="total",
        title="Contest Types"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )

with right:

    df = get_contest_phase_distribution()

    fig = px.pie(
        df,
        names="contest_phase",
        values="total",
        title="Contest Phases"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )

df = get_longest_contests()

fig = px.bar(
    df,
    x="duration_hours",
    y="contest_name",
    orientation="h",
    title="Top 20 Longest Contests"
)

st.plotly_chart(
    fig,
    use_container_width=True,
    config={"displayModeBar": False}
)

st.subheader("Recent Contests")

df = get_recent_contests()

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)