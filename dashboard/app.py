import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv


# Absolute path to project root
BASE_DIR = Path(__file__).resolve().parents[2]

# Load .env from python folder
load_dotenv(BASE_DIR / "python" / ".env")


def get_connection():

    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )



# import streamlit as st

# from queries.dashboard_queries import get_dashboard_kpis

# st.set_page_config(
#     page_title="Codeforces Analytics Platform",
#     page_icon="📈",
#     layout="wide"
# )

# st.title("Codeforces Analytics Platform")

# df = get_dashboard_kpis()

# st.dataframe(df)
import streamlit as st

st.set_page_config(
    page_title="Codeforces Analytics Platform",
    page_icon="📊",
    layout="wide"
)

st.title("Codeforces Analytics Platform")

st.write("Select a page from the sidebar.")