from repositories.user_repository import UserRepository

class UserFunctions:
    def __init__(self):
        self._user = None
        self._users = UserRepository()

    def log_in(self, username):
        if self._users.search_user(username):
            self._user = username
            return True
        return False

    def new_user(self, username):
        if self._users.search_user(username):
            return False
        self._users.add_user(username)
        return True

    def log_out(self):
        self._user = None