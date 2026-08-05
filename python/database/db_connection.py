import os
import mysql.connector

from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv()


def get_connection():
    """
    Create and return a MySQL database connection.
    """

    try:

        connection = mysql.connector.connect(

            host=os.getenv("DB_HOST"),

            port=int(os.getenv("DB_PORT")),

            user=os.getenv("DB_USER"),

            password=os.getenv("DB_PASSWORD"),

            database=os.getenv("DB_NAME")

        )

        return connection

    except mysql.connector.Error as err:

        print(f"Database Connection Error: {err}")

        return None