import streamlit as st

from queries.dashboard_queries import get_dashboard_kpis

from components.cards import show_metric


st.title("Dashboard")

df = get_dashboard_kpis()

col1, col2, col3, col4 = st.columns(4)

with col1:
    show_metric("Users", df["users"][0])

with col2:
    show_metric("Contests", df["contests"][0])

with col3:
    show_metric("Problems", df["problems"][0])

with col4:
    show_metric("Submissions", df["submissions"][0])


import plotly.express as px

from queries.dashboard_queries import get_rating_history

rating_df = get_rating_history()

fig = px.line(
    rating_df,
    x="rating_update_time",
    y="new_rating",
    markers=True,
    title="Rating Progress"
)

fig.update_layout(
    xaxis_title="Contest Date",
    yaxis_title="Rating",
    template="plotly_white",
    hovermode="x unified"
)
fig.update_traces(
    line=dict(width=3),
    marker=dict(size=6)
)

st.plotly_chart(
    fig,
    use_container_width=True,
    config={"displayModeBar": True}
)


from queries.dashboard_queries import get_verdict_distribution
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

left, right = st.columns(2)

with left:

    rating_df = get_rating_history()

    fig = px.line(
        rating_df,
        x="rating_update_time",
        y="new_rating",
        markers=True,
        title="Rating Progress"
    )

    fig.update_layout(
        template="plotly_white",
        hovermode="x unified"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": True}
    )


with right:

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
        config={"displayModeBar": True}
    )


    from queries.dashboard_queries import get_language_distribution
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
    config={"displayModeBar": True}
)