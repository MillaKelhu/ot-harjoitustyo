from database_connection import get_database_connection


class UserDatabase:
    def __init__(self, connection):
        self._db = connection
        self._db.isolation_level = None

    def search_user(self, username):
        user = self._db.execute(
            "SELECT * FROM users WHERE username=?", [username]).fetchone()

        return user

    def add_user(self, username):
        user_exists = self.search_user(username)

        if user_exists is None:
            self._db.execute(
                "INSERT INTO users (username) VALUES (?)", [username])

        return not bool(user_exists)

    def erase_all_users(self):
        cursor = self._db.cursor()

        cursor.execute("DELETE FROM users")

        self._db.commit()


user_database = UserDatabase(get_database_connection())
