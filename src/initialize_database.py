from database_connection import get_database_connection


def drop_tables(connection):
    """Deletes existing data tables in database.

    Args:
        connection (Connection): Connection to SQL-database.
    """

    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("DROP TABLE IF EXISTS recipes")

    connection.commit()


def create_tables(connection):
    """Creates tables users and recipes into database.

    Args:
        connection (Connection): Connection to SQL-database.
    """

    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE users
                    (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)''')
    cursor.execute('''CREATE TABLE recipes
                    (id INTEGER PRIMARY KEY, user_id INTEGER REFERENCES users, 
                    name TEXT, instructions TEXT)''')

    connection.commit()


def initialize_database():
    """Initializes the database by establishing a connection
    to SQL-database, and then creating new data tables.
    """

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


initialize_database()
