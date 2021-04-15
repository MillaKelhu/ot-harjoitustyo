from datacontrol.users_database import user_database as default_user_database
from datacontrol.recipes_database import recipes_database as default_recipes_database


class CookbookAppFunctions:
    def __init__(
        self,
        user_database=default_user_database,
        recipes_database=default_recipes_database
    ):
        self._user = None
        self._chosen_recipe = None
        self._users = user_database
        self._recipes = recipes_database

    def log_in(self, username):
        user = self._users.search_user(username)

        if user:
            self._user = user

        return bool(self._user)

    def log_out(self):
        self._user = None
        return True

    def sign_in(self, username):
        user_added = self._users.add_user(username)
        return user_added

    def current_user(self):
        return self._user

    def users_recipes(self):
        recipes = self._recipes.search_users_recipes(self._user[0])
        return recipes

    def add_recipes(self, name, instructions):
        self._recipes.add_recipe(self._user[0], name, instructions)
        return True

    def set_chosen_recipe(self, recipe_name):
        self._chosen_recipe = self._recipes.search_recipe(
            self._user[0], recipe_name)

        return bool(self._chosen_recipe)

    def get_chosen_recipe(self):
        return self._chosen_recipe

    def no_chosen_recipe(self):
        self._chosen_recipe = None
        return True


cookbookapp_functions = CookbookAppFunctions()
