import pandas as pd
from database.db import get_connection


def get_contest_type_distribution():

    connection = get_connection()

    query = """
    SELECT
        contest_type,
        COUNT(*) AS total
    FROM contests
    GROUP BY contest_type;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df


def get_contest_phase_distribution():

    connection = get_connection()

    query = """
    SELECT
        contest_phase,
        COUNT(*) AS total
    FROM contests
    GROUP BY contest_phase;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df


def get_longest_contests():

    connection = get_connection()

    query = """
    SELECT
        contest_name,
        duration_seconds / 3600 AS duration_hours
    FROM contests
    ORDER BY duration_seconds DESC
    LIMIT 20;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df


def get_recent_contests():

    connection = get_connection()

    query = """
    SELECT
        contest_name,
        contest_type,
        contest_phase,
        start_time
    FROM contests
    ORDER BY start_time DESC
    LIMIT 20;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df