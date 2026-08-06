import os
from dotenv import load_dotenv

from etl.load_users import load_user
from etl.load_contests import load_contests
from etl.load_problems import load_problems
from etl.load_problem_tags import load_problem_tags
from etl.load_submissions import load_submissions
from etl.load_rating_history import load_rating_history

load_dotenv()

def main():

    handle = os.getenv("CF_HANDLE")
    handle = os.getenv("CF_HANDLE")

    if not handle:
        print("❌ CF_HANDLE not found in .env")
        return

    print("=" * 70)
    print("      CODEFORCES ANALYTICS PLATFORM - ETL PIPELINE")
    print("=" * 70)

    print("\n[1/6] Loading User...")
    load_user(handle)

    print("\n[2/6] Loading Contests...")
    load_contests()

    print("\n[3/6] Loading Problems...")
    load_problems()

    print("\n[4/6] Loading Problem Tags...")
    load_problem_tags()

    print("\n[5/6] Loading Submissions...")
    load_submissions(handle)

    print("\n[6/6] Loading Rating History...")
    load_rating_history(handle)

    print("\n" + "=" * 70)
    print("ETL Pipeline Completed Successfully.")
    print("=" * 70)


if __name__ == "__main__":
    main()