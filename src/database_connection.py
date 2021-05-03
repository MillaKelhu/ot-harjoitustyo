import os
import sqlite3
import dotenv

dirname = os.path.dirname(__file__)

dotenv.load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))

database_name = os.getenv('database_name')

connection = sqlite3.connect(os.path.join(
    dirname, "..", "data", database_name))


def get_database_connection():
    """Returns the necessary connection to the correct SQL-database.
    While testing, the database is test-database.

    Returns:
        Connection: connection to SQL-database
    """

    return connection
