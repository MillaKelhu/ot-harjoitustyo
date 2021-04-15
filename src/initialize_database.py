from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("DROP TABLE IF EXISTS recipes")

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY, username TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS recipes
                    (id INTEGER PRIMARY KEY, user_id INTEGER, name TEXT, instructions TEXT)''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


initialize_database()
