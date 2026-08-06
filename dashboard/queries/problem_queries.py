import pandas as pd
from database.db import get_connection


def get_problem_rating_distribution():

    connection = get_connection()

    query = """
    SELECT
        problem_rating,
        COUNT(*) AS total
    FROM problems
    WHERE problem_rating IS NOT NULL
    GROUP BY problem_rating
    ORDER BY problem_rating;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df


def get_problem_type_distribution():

    connection = get_connection()

    query = """
    SELECT
        problem_type,
        COUNT(*) AS total
    FROM problems
    GROUP BY problem_type
    ORDER BY total DESC;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df


def get_top_hardest_problems():

    connection = get_connection()

    query = """
    SELECT
        problem_name,
        problem_rating,
        contest_id,
        problem_index
    FROM problems
    WHERE problem_rating IS NOT NULL
    ORDER BY problem_rating DESC
    LIMIT 20;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df


def get_problem_statistics():

    connection = get_connection()

    query = """
    SELECT
        COUNT(*) AS total_problems,
        AVG(problem_rating) AS average_rating,
        MAX(problem_rating) AS highest_rating,
        MIN(problem_rating) AS lowest_rating
    FROM problems
    WHERE problem_rating IS NOT NULL;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df