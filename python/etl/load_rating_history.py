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
        (handle,),
    )

    result = cursor.fetchone()

    if result is None:
      print(f"User '{handle}' not found.")
      return

    user_id = result[0]

    # ---------------------------------------
    # Batch Process rating history
    # ---------------------------------------
    upsert_query = """
            INSERT INTO rating_history (
                user_id,
                contest_id,
                contest_rank,
                old_rating,
                new_rating,
                rating_update_time,
                source
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                contest_rank = VALUES(contest_rank),
                old_rating = VALUES(old_rating),
                new_rating = VALUES(new_rating),
                rating_update_time = VALUES(rating_update_time),
                updated_at = CURRENT_TIMESTAMP;
        """

    batch_data = []

    for rating in ratings:
      rating_time = datetime.fromtimestamp(rating["ratingUpdateTimeSeconds"])

      batch_data.append((
          user_id,
          rating["contestId"],
          rating["rank"],
          rating["oldRating"],
          rating["newRating"],
          rating_time,
          "Codeforces",
      ))

    if batch_data:
      # Send all rating history records in a single payload
      cursor.executemany(upsert_query, batch_data)
      connection.commit()
      print(
          f"✅ {len(batch_data)} rating history records inserted/updated"
          " successfully in batch."
      )
    else:
      print("No rating history records found to insert.")

  except Exception as e:

    connection.rollback()

    print("Error during batch insert:", e)

  finally:

    cursor.close()
    connection.close()


if __name__ == "__main__":

  load_rating_history("tourist")