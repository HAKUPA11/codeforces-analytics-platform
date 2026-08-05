from datetime import datetime

from api.codeforces_api import get_user_submissions
from database.db_connection import get_connection


def load_submissions(handle):

    submissions = get_user_submissions(handle)

    if submissions is None:
        print("Failed to fetch submissions.")
        return

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = connection.cursor()

    processed = 0

    try:

        # ---------------------------------------
        # Get user_id from database
        # ---------------------------------------

        cursor.execute(
            """
            SELECT user_id
            FROM users
            WHERE handle = %s
            """,
            (handle,)
        )

        result = cursor.fetchone()

        if result is None:
            print(f"User '{handle}' not found.")
            return

        user_id = result[0]

        # ---------------------------------------
        # Process each submission
        # ---------------------------------------

        for submission in submissions:

            if "contestId" not in submission:
                continue

            if "problem" not in submission:
                continue

            contest_id = submission["contestId"]

            problem_index = submission["problem"]["index"]

            # ---------------------------------------
            # Find problem_id
            # ---------------------------------------

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

            problem = cursor.fetchone()

            if problem is None:
                continue

            problem_id = problem[0]

            # ---------------------------------------
            # Convert timestamp
            # ---------------------------------------

            submission_time = datetime.fromtimestamp(
                submission["creationTimeSeconds"]
            )

            # ---------------------------------------
            # Call procedure
            # ---------------------------------------

            cursor.callproc(
                "sp_add_submission",
                (
                    submission["id"],
                    user_id,
                    contest_id,
                    problem_id,
                    submission["programmingLanguage"],
                    submission.get("verdict"),
                    submission.get("passedTestCount", 0),
                    submission.get("timeConsumedMillis"),
                    submission.get("memoryConsumedBytes"),
                    submission_time,
                    submission.get("relativeTimeSeconds"),
                    "Codeforces"
                )
            )

            processed += 1

        connection.commit()

        print(
            f"✅ {processed} submissions inserted successfully."
        )

    except Exception as e:

        connection.rollback()

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()