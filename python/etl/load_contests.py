from datetime import datetime

from api.codeforces_api import get_contest_list
from database.db_connection import get_connection


def load_contests():

    contests = get_contest_list()

    if contests is None:
        print("Failed to fetch contests.")
        return

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = connection.cursor()

    inserted = 0

    try:

        for contest in contests:

            start_time = None

            if "startTimeSeconds" in contest:

                start_time = datetime.fromtimestamp(
                    contest["startTimeSeconds"]
                )

            cursor.callproc(
                "sp_upsert_contest",
                (
                    contest["id"],
                    contest["name"],
                    contest["type"],
                    contest["phase"],
                    contest["frozen"],
                    contest["durationSeconds"],
                    start_time,
                    "Codeforces"
                )
            )

            inserted += 1

        connection.commit()

        print(f"✅ {inserted} contests inserted/updated successfully.")

    except Exception as e:

        connection.rollback()

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()


if __name__ == "__main__":

    load_contests()