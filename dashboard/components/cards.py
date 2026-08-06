import streamlit as st


def show_metric(label, value):

    st.metric(
        label=label,
        value=value
    )