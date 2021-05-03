from database_connection import get_database_connection


class UserDatabase:
    """Class that oversees and controls the SQL-database in which all users are saved

    Attributes:
        _db: connection to SQL-database
    """

    def __init__(self, connection):
        """Constructor of class that establishes the connection to SQL-database.

        Args:
            connection (Connection): Connection to SQL-database.
        """

        self._db = connection
        self._db.isolation_level = None

    def search_user(self, username, password=None):
        """Searches and returns a row containing given arguments from data table users.

        Args:
            username (string): The user's username.
            password (string, optional): The user's password. Defaults to None.

        Returns:
            tuple or None: Depending on the result of the query, the function returns:
            a tuple that contains the id, username and password;
            None, if a row with given arguments does not exist.
        """

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
        """Adds a row into data table users.

        Args:
            username (string): A new user's username
            password (string): A new user's password.

        Returns:
            boolean: Variable user_exists contains the result of function search_user
            with the given arguments, and that is turned into a boolean.
            The function returns the opposite of this boolean, signifying whether or not
            a new row, and thus a user, was added successfully.
        """

        user_exists = self.search_user(username)

        if user_exists is None:
            self._db.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)", [username, password])

        return not bool(user_exists)

    def erase_all_users(self):
        """Deletes all rows from data table users.
        """

        cursor = self._db.cursor()

        cursor.execute("DELETE FROM users")

        self._db.commit()

    def get_all_users(self):
        """Searches and returns all rows in data table users.

        Returns:
            list or None: Depending on the resluts of the query, the function returns:
            a list containing the table's rows as tuples;
            None, if the table is empty.
        """

        users = self._db.execute(
            "SELECT * FROM users").fetchall()

        if users == []:
            users = None

        return users


user_database = UserDatabase(get_database_connection())
