# from database.db_connection import get_connection


# def main():

#     connection = get_connection()

#     if connection is None:

#         print("❌ Failed to connect to database.")
#         return

#     print("=" * 60)
#     print("✅ Successfully Connected to MySQL")
#     print("=" * 60)

#     cursor = connection.cursor()

#     cursor.execute("SELECT DATABASE();")

#     database = cursor.fetchone()

#     print(f"Current Database : {database[0]}")

#     cursor.close()

#     connection.close()

#     print("\n🔒 Connection Closed Successfully")


# if __name__ == "__main__":
#     main()




# from etl.load_users import load_user
# def main():

#     load_user("tourist")


# if __name__ == "__main__":
#     main()



# from etl.load_contests import load_contests
# def main():

#     load_contests()


# if __name__ == "__main__":
#     main()



# from etl.load_problems import load_problems
# def main():

#     load_problems()


# if __name__ == "__main__":
#     main()

# from etl.load_problem_tags import load_problem_tags


# def main():

#     load_problem_tags()


# if __name__ == "__main__":
#     main()


# from etl.load_submissions import load_submissions


# def main():

#     load_submissions("tourist")


# if __name__ == "__main__":
#     main()


from etl.load_rating_history import load_rating_history


def main():

    load_rating_history("tourist")


if __name__ == "__main__":
    main()

