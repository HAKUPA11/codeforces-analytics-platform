import streamlit as st
import plotly.express as px

from queries.rating_queries import *

st.set_page_config(
    page_title="Rating Analytics",
    page_icon="📈",
    layout="wide"
)

st.title("Rating Analytics")

timeline = get_rating_timeline()

fig = px.line(
    timeline,
    x="rating_update_time",
    y="new_rating",
    markers=True,
    title="Rating Timeline"
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

distribution = get_rating_change_distribution()

fig = px.histogram(
    distribution,
    x="rating_change",
    nbins=20,
    title="Rating Change Distribution"
)

fig.update_layout(
    template="plotly_white"
)

st.plotly_chart(
    fig,
    use_container_width=True,
    config={"displayModeBar": False}
)    


left, right = st.columns(2)

with left:

    st.subheader("Biggest Rating Gains")

    st.dataframe(
        get_biggest_gains(),
        hide_index=True,
        use_container_width=True
    )

with right:

    st.subheader("Biggest Rating Losses")

    st.dataframe(
        get_biggest_losses(),
        hide_index=True,
        use_container_width=True
    )


st.subheader("Complete Rating History")

st.dataframe(
    get_rating_history_table(),
    hide_index=True,
    use_container_width=True
)