import pandas as pd
from database.db import get_connection


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
        city,
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
        c.contest_name,
        r.old_rating,
        r.new_rating,
        r.rating_change,
        r.rating_update_time
    FROM rating_history r
    JOIN contests c
        ON r.contest_id = c.contest_id
    ORDER BY r.rating_update_time;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df


def get_rating_summary():

    connection = get_connection()

    query = """
    SELECT
        current_rating,
        highest_rating,
        highest_rating-current_rating AS rating_gap
    FROM users
    LIMIT 1;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df