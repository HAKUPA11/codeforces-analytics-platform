from datetime import datetime

from api.codeforces_api import get_user_rating
from database.db_connection import get_connection


def load_rating_history(handle):

    ratings = get_user_rating(handle)

    if ratings is None:
        print("Failed to fetch rating history.")
        return

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = connection.cursor()

    processed = 0

    try:

        # ---------------------------------------
        # Get user_id
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
        # Process rating history
        # ---------------------------------------

        for rating in ratings:

            rating_time = datetime.fromtimestamp(
                rating["ratingUpdateTimeSeconds"]
            )

            cursor.callproc(
                "sp_add_rating_history",
                (
                    user_id,
                    rating["contestId"],
                    rating["rank"],
                    rating["oldRating"],
                    rating["newRating"],
                    rating_time,
                    "Codeforces"
                )
            )

            processed += 1

        connection.commit()

        print(
            f"✅ {processed} rating history records inserted successfully."
        )

    except Exception as e:

        connection.rollback()

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()