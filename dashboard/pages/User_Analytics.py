import streamlit as st
import plotly.express as px

from queries.user_queries import (
    get_user_profile,
    get_rating_history,
    get_rating_summary
)

st.set_page_config(
    page_title="User Analytics",
    page_icon="👤",
    layout="wide"
)

st.title("User Analytics")

# --------------------------------------------------
# User Profile
# --------------------------------------------------

profile = get_user_profile()

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Handle",
        profile["handle"][0]
    )

    st.metric(
        "Current Rating",
        profile["current_rating"][0]
    )

    st.metric(
        "Highest Rating",
        profile["highest_rating"][0]
    )

with col2:

    st.metric(
        "Current Rank",
        profile["current_rank"][0]
    )

    st.metric(
        "Highest Rank",
        profile["highest_rank"][0]
    )

    st.metric(
        "Country",
        profile["country"][0]
    )

# --------------------------------------------------
# Rating Summary
# --------------------------------------------------

summary = get_rating_summary()

st.subheader("Rating Summary")

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "Current Rating",
        summary["current_rating"][0]
    )

with c2:

    st.metric(
        "Highest Rating",
        summary["highest_rating"][0]
    )

with c3:

    st.metric(
        "Rating Gap",
        summary["rating_gap"][0]
    )

# --------------------------------------------------
# Rating Progress
# --------------------------------------------------

rating_history = get_rating_history()

fig = px.line(
    rating_history,
    x="rating_update_time",
    y="new_rating",
    markers=True,
    title="Rating Progress"
)

fig.update_layout(
    template="plotly_white",
    xaxis_title="Contest Date",
    yaxis_title="Rating",
    hovermode="x unified"
)

fig.update_traces(
    line=dict(width=3),
    marker=dict(size=6)
)

st.plotly_chart(
    fig,
    use_container_width=True,
    config={"displayModeBar": False}
)

# --------------------------------------------------
# Rating History Table
# --------------------------------------------------

st.subheader("Rating History")

st.dataframe(
    rating_history,
    use_container_width=True,
    hide_index=True
)