import os
from pathlib import Path

import mysql.connector
import streamlit as st
from dotenv import load_dotenv

# Project root directory
BASE_DIR = Path(__file__).resolve().parents[2]

# Load .env from project root for local development
load_dotenv(BASE_DIR / ".env")


def get_connection():
  # 1. Try fetching from environment variables (.env)
  # 2. Fall back to st.secrets for Streamlit Cloud deployment
  host = (
      os.getenv("DB_HOST")
      or st.secrets.get("DB_HOST")
      or st.secrets.get("mysql", {}).get("DB_HOST")
  )
  port = (
      os.getenv("DB_PORT")
      or st.secrets.get("DB_PORT")
      or st.secrets.get("mysql", {}).get("DB_PORT")
      or "3306"
  )
  user = (
      os.getenv("DB_USER")
      or st.secrets.get("DB_USER")
      or st.secrets.get("mysql", {}).get("DB_USER")
  )
  password = (
      os.getenv("DB_PASSWORD")
      or st.secrets.get("DB_PASSWORD")
      or st.secrets.get("mysql", {}).get("DB_PASSWORD")
  )
  database = (
      os.getenv("DB_NAME")
      or st.secrets.get("DB_NAME")
      or st.secrets.get("mysql", {}).get("DB_NAME")
  )

  return mysql.connector.connect(
      host=host,
      port=int(port),
      user=user,
      password=password,
      database=database,
      connect_timeout=60,
  )