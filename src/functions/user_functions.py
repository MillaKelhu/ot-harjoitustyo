from datacontrol.users_database import UserDatabase

class UserFunctions:
    def __init__(self):
        self._user = None
        self._users = UserDatabase()

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

if __name__ == "__main__":
    ui = UserFunctions()
    print(ui.log_in("Milla")) # True
    print(ui.log_in("Jouko")) # False
    print(ui.sign_in("Milla")) # False
    print(ui.sign_in("Jouko")) # True
    print(ui.log_out()) # True
    print(ui.log_in("")) #False