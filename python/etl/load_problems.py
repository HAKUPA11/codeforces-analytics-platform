from api.codeforces_api import get_problemset
from database.db_connection import get_connection


def load_problems():

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

            # Ignore problems without contestId
            if "contestId" not in problem:
                continue


            cursor.callproc(
                "sp_upsert_problem",
                (
                    problem["contestId"],

                    problem["index"],

                    problem["name"],

                    problem.get("type"),

                    problem.get("points"),

                    problem.get("rating"),

                    problem.get("rating") is not None,

                    "Codeforces"
                )
            )

            processed += 1


        connection.commit()

        print(
            f"✅ {processed} problems inserted/updated successfully."
        )


    except Exception as e:

        connection.rollback()

        print("Error:", e)


    finally:

        cursor.close()
        connection.close()