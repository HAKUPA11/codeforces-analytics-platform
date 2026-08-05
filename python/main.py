from database.db_connection import get_connection


def main():

    connection = get_connection()

    if connection is None:

        print("❌ Failed to connect to database.")
        return

    print("=" * 60)
    print("✅ Successfully Connected to MySQL")
    print("=" * 60)

    cursor = connection.cursor()

    cursor.execute("SELECT DATABASE();")

    database = cursor.fetchone()

    print(f"Current Database : {database[0]}")

    cursor.close()

    connection.close()

    print("\n🔒 Connection Closed Successfully")


if __name__ == "__main__":
    main()