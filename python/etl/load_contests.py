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

  # High-performance batch upsert query
  upsert_query = """
        INSERT INTO contests (
            contest_id,
            contest_name,
            contest_type,
            contest_phase,
            is_frozen,
            duration_seconds,
            start_time,
            source
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            contest_name = VALUES(contest_name),
            contest_type = VALUES(contest_type),
            contest_phase = VALUES(contest_phase),
            is_frozen = VALUES(is_frozen),
            duration_seconds = VALUES(duration_seconds),
            start_time = VALUES(start_time),
            updated_at = CURRENT_TIMESTAMP;
    """

  batch_data = []

  for contest in contests:
    start_time = None

    if "startTimeSeconds" in contest:
      start_time = datetime.fromtimestamp(contest["startTimeSeconds"])

    batch_data.append((
        contest["id"],
        contest["name"],
        contest["type"],
        contest["phase"],
        contest["frozen"],
        contest["durationSeconds"],
        start_time,
        "Codeforces",
    ))

  try:
    # Sends all contests in a single network payload
    cursor.executemany(upsert_query, batch_data)

    connection.commit()

    print(
        f"✅ {len(batch_data)} contests inserted/updated successfully in batch."
    )

  except Exception as e:

    connection.rollback()

    print("Error during batch insert:", e)

  finally:

    cursor.close()
    connection.close()


if __name__ == "__main__":

  load_contests()