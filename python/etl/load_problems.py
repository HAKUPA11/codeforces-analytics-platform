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

  # High-performance batch upsert query
  upsert_query = """
        INSERT INTO problems (
            contest_id,
            problem_index,
            problem_name,
            problem_type,
            points,
            problem_rating,
            is_rated,
            source
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            problem_name = VALUES(problem_name),
            problem_type = VALUES(problem_type),
            points = VALUES(points),
            problem_rating = VALUES(problem_rating),
            is_rated = VALUES(is_rated),
            updated_at = CURRENT_TIMESTAMP;
    """

  batch_data = []

  for problem in problems:
    # Ignore problems without contestId
    if "contestId" not in problem:
      continue

    batch_data.append((
        problem["contestId"],
        problem["index"],
        problem["name"],
        problem.get("type", "PROGRAMMING"),
        problem.get("points"),
        problem.get("rating"),
        problem.get("rating") is not None,
        "Codeforces",
    ))

  try:
    # Sends all 9,000+ problems in a single network payload
    cursor.executemany(upsert_query, batch_data)

    connection.commit()

    print(
        f"✅ {len(batch_data)} problems inserted/updated successfully in batch."
    )

  except Exception as e:

    connection.rollback()

    print("Error during batch insert:", e)

  finally:

    cursor.close()
    connection.close()


if __name__ == "__main__":

  load_problems()