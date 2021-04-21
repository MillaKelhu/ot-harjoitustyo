from database_connection import get_database_connection


class UserDatabase:
    def __init__(self, connection):
        self._db = connection
        self._db.isolation_level = None

    def search_user(self, username, password=None):
        if password:
            user = self._db.execute(
                "SELECT * FROM users WHERE username=? AND password=?", [
                    username, password]
            ).fetchone()
        else:
            user = self._db.execute(
                "SELECT * FROM users WHERE username=?", [username]).fetchone()

        return user

    def add_user(self, username, password):
        user_exists = self.search_user(username)

        if user_exists is None:
            self._db.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)", [username, password])

        return not bool(user_exists)

    def erase_all_users(self):
        cursor = self._db.cursor()

        cursor.execute("DELETE FROM users")

        self._db.commit()

    def get_all_users(self):
        users = self._db.execute(
            "SELECT * FROM users").fetchall()

        if users == []:
            users = None

        return users


user_database = UserDatabase(get_database_connection())
