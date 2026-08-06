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

  try:
    # ---------------------------------------------------------
    # 1. Fetch all problem mappings in ONE query
    # Map: (contest_id, problem_index) -> problem_id
    # ---------------------------------------------------------
    cursor.execute("""
            SELECT contest_id, problem_index, problem_id
            FROM problems
        """)
    problem_map = {
        (row[0], row[1]): row[2] for row in cursor.fetchall()
    }

    # ---------------------------------------------------------
    # 2. Extract all unique tag names from API response
    # ---------------------------------------------------------
    unique_tags = set()
    for problem in problems:
      tags = problem.get("tags", [])
      for tag in tags:
        unique_tags.add((tag,))  # Tuple format for executemany

    # Insert all tags in batch
    if unique_tags:
      cursor.executemany(
          "INSERT IGNORE INTO tags (tag_name) VALUES (%s)",
          list(unique_tags),
      )
      connection.commit()

    # Fetch updated tag_id mappings in ONE query
    # Map: tag_name -> tag_id
    cursor.execute("SELECT tag_name, tag_id FROM tags")
    tag_map = {row[0]: row[1] for row in cursor.fetchall()}

    # ---------------------------------------------------------
    # 3. Build problem_tags relationships in memory
    # ---------------------------------------------------------
    problem_tags_batch = set()
    processed_problems = 0

    for problem in problems:
      if "contestId" not in problem:
        continue

      contest_id = problem["contestId"]
      problem_index = problem["index"]

      problem_id = problem_map.get((contest_id, problem_index))
      if problem_id is None:
        continue

      tags = problem.get("tags", [])
      if not tags:
        continue

      for tag in tags:
        tag_id = tag_map.get(tag)
        if tag_id is not None:
          problem_tags_batch.add((problem_id, tag_id))

      processed_problems += 1

    # ---------------------------------------------------------
    # 4. Insert all problem-tag relations in ONE payload
    # ---------------------------------------------------------
    if problem_tags_batch:
      cursor.executemany(
          """
                INSERT IGNORE INTO problem_tags (problem_id, tag_id)
                VALUES (%s, %s)
            """,
          list(problem_tags_batch),
      )
      connection.commit()

      print(
          f"✅ Tags mapped for {processed_problems} problems successfully in batch!"
      )
    else:
      print("No problem tags found to insert.")

  except Exception as e:

    connection.rollback()

    print("Error during batch insert:", e)

  finally:

    cursor.close()
    connection.close()


if __name__ == "__main__":

  load_problem_tags()