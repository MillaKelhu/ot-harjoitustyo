from datacontrol.users_database import user_database as default_user_database

class UserFunctions:
    def __init__(self, user_database=default_user_database):
        self._user = None
        self._users = user_database

    def log_in(self, username):

        if self._users.search_user(username):
            self._user = username
            return True

        else:
            return False

    def log_out(self):
        self._user = None
        return True

    def sign_in(self, username):
        user_added = self._users.add_user(username)
        return(user_added)

    def current_user(self):
        return self._user

user_functions = UserFunctions()