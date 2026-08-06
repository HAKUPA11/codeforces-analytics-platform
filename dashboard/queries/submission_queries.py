import pandas as pd
from database.db import get_connection


def get_verdict_distribution():

    connection = get_connection()

    query = """
    SELECT
        verdict,
        COUNT(*) AS total
    FROM submissions
    GROUP BY verdict
    ORDER BY total DESC;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df


def get_language_distribution():

    connection = get_connection()

    query = """
    SELECT
        programming_language,
        COUNT(*) AS total
    FROM submissions
    GROUP BY programming_language
    ORDER BY total DESC;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df


def get_submission_timeline():

    connection = get_connection()

    query = """
    SELECT
        DATE(submission_time) AS submission_date,
        COUNT(*) AS total_submissions
    FROM submissions
    GROUP BY DATE(submission_time)
    ORDER BY submission_date;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df


def get_recent_submissions():

    connection = get_connection()

    query = """
    SELECT
        submission_id,
        verdict,
        programming_language,
        execution_time_ms,
        memory_bytes,
        submission_time
    FROM submissions
    ORDER BY submission_time DESC
    LIMIT 20;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df