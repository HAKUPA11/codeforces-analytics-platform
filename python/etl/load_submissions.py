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

  try:
    # ---------------------------------------------------------
    # 1. Fetch user_id
    # ---------------------------------------------------------
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

    # ---------------------------------------------------------
    # 2. Fetch all problems mapping in ONE query (Fast Lookup)
    # ---------------------------------------------------------
    cursor.execute("""
            SELECT contest_id, problem_index, problem_id
            FROM problems
        """)

    # Map: (contest_id, problem_index) -> problem_id
    problem_map = {
        (row[0], row[1]): row[2] for row in cursor.fetchall()
    }

    # ---------------------------------------------------------
    # 3. Prepare Submissions Batch Data
    # ---------------------------------------------------------
    upsert_query = """
            INSERT INTO submissions (
                submission_id,
                user_id,
                contest_id,
                problem_id,
                programming_language,
                verdict,
                passed_test_count,
                execution_time_ms,
                memory_bytes,
                submission_time,
                relative_time_seconds,
                source
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                verdict = VALUES(verdict),
                passed_test_count = VALUES(passed_test_count),
                execution_time_ms = VALUES(execution_time_ms),
                memory_bytes = VALUES(memory_bytes),
                updated_at = CURRENT_TIMESTAMP;
        """

    batch_data = []

    for submission in submissions:
      if "contestId" not in submission or "problem" not in submission:
        continue

      contest_id = submission["contestId"]
      problem_index = submission["problem"]["index"]

      # Instant dictionary lookup without network roundtrips
      problem_id = problem_map.get((contest_id, problem_index))

      if problem_id is None:
        continue

      submission_time = datetime.fromtimestamp(
          submission["creationTimeSeconds"]
      )

      batch_data.append((
          submission["id"],
          user_id,
          contest_id,
          problem_id,
          submission["programmingLanguage"],
          submission.get("verdict", "TESTING"),
          submission.get("passedTestCount", 0),
          submission.get("timeConsumedMillis"),
          submission.get("memoryConsumedBytes"),
          submission_time,
          submission.get("relativeTimeSeconds"),
          "Codeforces",
      ))

    # ---------------------------------------------------------
    # 4. Execute Batch Payload
    # ---------------------------------------------------------
    if batch_data:
      cursor.executemany(upsert_query, batch_data)
      connection.commit()
      print(
          f"✅ {len(batch_data)} submissions inserted/updated successfully in batch."
      )
    else:
      print("No valid submissions found to insert.")

  except Exception as e:

    connection.rollback()

    print("Error during batch insert:", e)

  finally:

    cursor.close()
    connection.close()


if __name__ == "__main__":

  load_submissions("tourist")