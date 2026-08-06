import pandas as pd
from database.db import get_connection


def get_rating_change_distribution():

    connection = get_connection()

    query = """
    SELECT
        rating_change
    FROM rating_history
    ORDER BY rating_update_time;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df


def get_rating_timeline():

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


def get_biggest_gains():

    connection = get_connection()

    query = """
    SELECT
        c.contest_name,
        contest_rank,
        old_rating,
        new_rating,
        rating_change
    FROM rating_history r
    JOIN contests c
        ON r.contest_id = c.contest_id
    ORDER BY rating_change DESC
    LIMIT 10;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df


def get_biggest_losses():

    connection = get_connection()

    query = """
    SELECT
        c.contest_name,
        contest_rank,
        old_rating,
        new_rating,
        rating_change
    FROM rating_history r
    JOIN contests c
        ON r.contest_id = c.contest_id
    ORDER BY rating_change ASC
    LIMIT 10;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df


def get_rating_history_table():

    connection = get_connection()

    query = """
    SELECT
        c.contest_name,
        contest_rank,
        old_rating,
        new_rating,
        rating_change,
        rating_update_time
    FROM rating_history r
    JOIN contests c
        ON r.contest_id = c.contest_id
    ORDER BY rating_update_time DESC;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df