import sqlite3

class UserRepository:
    def __init__(self):
        self._db = sqlite3.connect("users.db")
        self._db.isolation_level = None

        self._table_exists()

    def _table_exists(self):
        tables = self._db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Users'").fetchall()
        if tables != []:
            return 
        self._table_Users()

    def _table_Users(self):
        self._db.execute("CREATE TABLE Users (id INTEGER PRIMARY KEY, username TEXT)")

    def search_user(self, username):
        user = self._db.execute("SELECT * FROM Users WHERE username=?", [username]).fetchall()
        if user:
            return True
        return False

    def add_user(self, username):
        if self.search_user(username):
            return
        self._db.execute("INSERT INTO Users (username) VALUES (?)", [username])

if __name__ == "__main__":
    udb = UserRepository()
    #print(udb.search_user("Milla"))
    #udb.add_user("Milla")
    #udb.add_user("Milla")
    #print(udb.search_user("Milla"))

