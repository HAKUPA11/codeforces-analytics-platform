from api.codeforces_api import get_user_info
from database.db_connection import get_connection


def load_user(handle):
    """
    Fetch a user's data from the Codeforces API
    and store it in the database.
    """

    user_data = get_user_info(handle)

    if not user_data:
        print("Failed to fetch user.")
        return

    user = user_data[0]

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = connection.cursor()

    try:

        cursor.callproc(
            "sp_upsert_user",
            (
                user["handle"],
                user.get("rank"),
                user.get("maxRank"),
                user.get("rating"),
                user.get("maxRating"),
                user.get("contribution", 0),
                user.get("friendOfCount", 0),
                user.get("organization"),
                user.get("country"),
                user.get("city"),
                "Codeforces"
            )
        )

        connection.commit()

        print(f"✅ User '{handle}' inserted/updated successfully.")

    except Exception as e:

        connection.rollback()

        print("Error:", e)

    finally:

        cursor.close()
        connection.close()


if __name__ == "__main__":

    load_user("tourist")