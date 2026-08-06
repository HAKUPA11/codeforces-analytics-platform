import pandas as pd
from database.db import get_connection


def get_top_tags():

    connection = get_connection()

    query = """
    SELECT
        t.tag_name,
        COUNT(*) AS total_problems
    FROM problem_tags pt
    JOIN tags t
        ON pt.tag_id = t.tag_id
    GROUP BY t.tag_name
    ORDER BY total_problems DESC;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df


def get_average_rating_per_tag():

    connection = get_connection()

    query = """
    SELECT
        t.tag_name,
        ROUND(AVG(p.problem_rating),2) AS average_rating
    FROM problem_tags pt
    JOIN tags t
        ON pt.tag_id = t.tag_id
    JOIN problems p
        ON pt.problem_id = p.problem_id
    WHERE p.problem_rating IS NOT NULL
    GROUP BY t.tag_name
    ORDER BY average_rating DESC;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df


def get_hardest_tags():

    connection = get_connection()

    query = """
    SELECT
        t.tag_name,
        MAX(p.problem_rating) AS hardest_problem
    FROM problem_tags pt
    JOIN tags t
        ON pt.tag_id = t.tag_id
    JOIN problems p
        ON pt.problem_id = p.problem_id
    WHERE p.problem_rating IS NOT NULL
    GROUP BY t.tag_name
    ORDER BY hardest_problem DESC;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df