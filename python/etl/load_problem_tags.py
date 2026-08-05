from api.codeforces_api import get_problemset
from database.db_connection import get_connection


def load_problem_tags():

    data = get_problemset()

    if data is None:
        print("Failed to fetch problems.")
        return

    problems = data["problems"]

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = connection.cursor()

    processed = 0

    try:

        for problem in problems:

            if "contestId" not in problem:
                continue


            contest_id = problem["contestId"]

            problem_index = problem["index"]


            # Get problem_id from database

            cursor.execute(
                """
                SELECT problem_id
                FROM problems
                WHERE contest_id = %s
                AND problem_index = %s
                """,
                (
                    contest_id,
                    problem_index
                )
            )


            result = cursor.fetchone()


            if result is None:
                continue


            problem_id = result[0]


            tags = problem.get("tags", [])

            if not tags:
                continue


            for tag in tags:


                # Insert tag

                cursor.callproc(
                    "sp_upsert_tag",
                    (
                        tag,
                    )
                )


                # Get tag_id

                cursor.execute(
                    """
                    SELECT tag_id
                    FROM tags
                    WHERE tag_name = %s
                    """,
                    (
                        tag,
                    )
                )


                tag_result = cursor.fetchone()


                if tag_result is None:
                    continue


                tag_id = tag_result[0]


                # Create problem-tag relation

                cursor.callproc(
                    "sp_add_problem_tag",
                    (
                        problem_id,
                        tag_id
                    )
                )


            processed += 1


        connection.commit()

        print(
            f"✅ Tags mapped for {processed} problems successfully."
        )


    except Exception as e:

        connection.rollback()

        print("Error:", e)


    finally:

        cursor.close()
        connection.close()