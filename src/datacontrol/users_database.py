import sqlite3

class UserDatabase:
    def __init__(self):
        self._db = sqlite3.connect("users.db")
        self._db.isolation_level = None

        self._table_Users_exists()

    def _table_Users_exists(self):
        self._db.execute("CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, username TEXT)")

    def search_user(self, username):
        user = self._db.execute("SELECT * FROM Users WHERE username=?", [username]).fetchone()

        return user

    def add_user(self, username):
        user_exists = self.search_user(username)

        if user_exists:
            return False
        else:
            self._db.execute("INSERT INTO Users (username) VALUES (?)", [username])
            return True

    def erase_all_users(self):
        self._db.execute("DROP TABLE Users")   
        self._table_Users_exists()     

user_database = UserDatabase()