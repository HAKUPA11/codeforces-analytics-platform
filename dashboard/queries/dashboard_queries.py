import pandas as pd

from database.db import get_connection


def get_dashboard_kpis():

    connection = get_connection()

    query = """
    SELECT
        (SELECT COUNT(*) FROM users) AS users,
        (SELECT COUNT(*) FROM contests) AS contests,
        (SELECT COUNT(*) FROM problems) AS problems,
        (SELECT COUNT(*) FROM submissions) AS submissions
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df

def get_user_profile():

    connection = get_connection()

    query = """
    SELECT
        handle,
        current_rating,
        highest_rating,
        current_rank,
        highest_rank,
        country,
        organization
    FROM users
    LIMIT 1;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df


def get_rating_history():

    connection = get_connection()

    query = """
    SELECT
        rating_update_time,
        new_rating
    FROM rating_history
    ORDER BY rating_update_time;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df


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