import streamlit as st
import plotly.express as px

from queries.problem_queries import (
    get_problem_rating_distribution,
    get_problem_type_distribution,
    get_top_hardest_problems,
    get_problem_statistics
)

st.set_page_config(
    page_title="Problem Analytics",
    page_icon="🧩",
    layout="wide"
)

st.title("Problem Analytics")

stats = get_problem_statistics()

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Problems", int(stats["total_problems"][0]))

with c2:
    st.metric("Average Rating", round(stats["average_rating"][0]))

with c3:
    st.metric("Highest Rating", int(stats["highest_rating"][0]))

with c4:
    st.metric("Lowest Rating", int(stats["lowest_rating"][0]))


left, right = st.columns(2)

with left:

    rating_df = get_problem_rating_distribution()

    fig = px.bar(
        rating_df,
        x="problem_rating",
        y="total",
        title="Problem Rating Distribution"
    )

    fig.update_layout(template="plotly_white")

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )


st.subheader("Top 20 Hardest Problems")

hard_df = get_top_hardest_problems()

st.dataframe(
    hard_df,
    use_container_width=True,
    hide_index=True
)