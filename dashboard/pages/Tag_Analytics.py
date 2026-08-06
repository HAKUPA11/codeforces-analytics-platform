import streamlit as st
import plotly.express as px

from queries.tag_queries import (
    get_top_tags,
    get_average_rating_per_tag,
    get_hardest_tags
)

st.set_page_config(
    page_title="Tag Analytics",
    page_icon="🏷️",
    layout="wide"
)

st.title("Tag Analytics")

left, right = st.columns(2)

with left:

    tag_df = get_top_tags()

    fig = px.bar(
        tag_df.head(15),
        x="tag_name",
        y="total_problems",
        title="Top 15 Tags"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Tag",
        yaxis_title="Problems"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )


with right:

    avg_df = get_average_rating_per_tag()

    fig = px.bar(
        avg_df.head(15),
        x="tag_name",
        y="average_rating",
        title="Average Rating per Tag"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Tag",
        yaxis_title="Average Rating"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )


st.subheader("Hardest Tags")

hard_df = get_hardest_tags()

st.dataframe(
    hard_df,
    use_container_width=True,
    hide_index=True
)