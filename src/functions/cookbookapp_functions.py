from datacontrol.users_database import user_database as default_user_database
from datacontrol.recipes_database import recipes_database as default_recipes_database


class CookbookAppFunctions:
    """Class that provides the necessary services and functions for a cookbook app.
    """

    def __init__(
        self,
        user_database=default_user_database,
        recipes_database=default_recipes_database
    ):
        """Constructor of class that establishes connection to
        the databases and keeps record of chosen user and recipe.

        Args:
            user_database (UserDatabase, optional): Functions to control
            the table users in SQL-database. Defaults to default_user_database.
            recipes_database (RecipesDatabase, optional): Functions to control
            the table recipes in SQL-database. Defaults to default_recipes_database.
        """

        self._user = None
        self._chosen_recipe = None
        self._users = user_database
        self._recipes = recipes_database

    def log_in(self, username, password):
        """Sets variable _user according to given arguments.

        Args:
            username (string): The username of the user trying to log in.
            password (string): The password of the user trying to log in.

        Returns:
            boolean: A boolean that informs whether or not an user with given arguments exists,
            and thus whether or not variable _user is set successfully.
        """

        if password:
            user = self._users.search_user(username, password)

            if user:
                self._user = user

        return bool(self._user)

    def log_out(self):
        """Sets variable _user as None.

        Returns:
            boolean: True
        """

        self._user = None
        return True

    def sign_in(self, username, password):
        """Creates a new user.

        Args:
            username (string): The username of the new user.
            password (string): The password of the new user.

        Returns:
            boolean: The returned boolean informs whether or not
            a new user was created successfully.
        """

        user_added = self._users.add_user(username, password)
        return user_added

    def current_user(self):
        """Returns the value of _user.

        Returns:
            tuple or None: The value of _user is either:
            a tuple containing the id, username and password of a user;
            None.
        """

        return self._user

    def users_recipes(self, keyword=None):
        """Returns all recipes in sql data table recipes where user id is that of variable _user's.

        Args:
            keyword (string, default None): A string variable used to filter the search results.
            If none are given, the query returns all user's recipes.

        Returns:
            list: List of tuples. Each tuple contains
            the recipe's id, user's id, recipe name, and instructions.
        """

        recipes = self._recipes.search_users_recipes(self._user[0], keyword)
        return recipes

    def add_recipes(self, name, instructions):
        """Adds a recipe in sql data table recipes with user id as that of variable _user's.

        Args:
            name (string): The name of the recipe.
            instructions (string): Instructions for the recipe.

        Returns:
            boolean: True.
        """

        self._recipes.add_recipe(self._user[0], name, instructions)
        return True

    def set_chosen_recipe(self, recipe_name):
        """Sets value for variable _chosen_recipe.

        Args:
            recipe_name (string): The name of the recipe.

        Returns:
            boolean: A boolean that informs whether or not a recipe with the given argument exists,
            and thus whether or not variable _chosen_recipe is set successfully.
        """

        self._chosen_recipe = self._recipes.search_recipe(
            self._user[0], recipe_name)

        return bool(self._chosen_recipe)

    def get_chosen_recipe(self):
        """Returns the value of _chosen_recipe.

        Returns:
            tuple or None: The value of _chosen_recipe is either:
            a tuple containing the id, the id of user who added the recipe,
            recipe name and instructions;
            None.
        """

        return self._chosen_recipe

    def no_chosen_recipe(self):
        """Sets the value of _chosen_recipe as None.

        Returns:
            boolean: True
        """

        self._chosen_recipe = None
        return True

    def modify_chosen_recipe(self, instructions):
        """Modifies the instructions of a row that matches _chosen_recipe in SQL data table recipes.

        Args:
            instructions (string): New instructions of the recipe.

        Returns:
            boolean: A boolean that informs whether or not the recipe was modified successfully.
            If _chosen_recipe is None, nothing could be modified, and the function returns False.
            If _chosen_recipe is not None, the recipe could be modified because function
            modify_recipe() is able to find a matching row from dat table recipes,
            and thus the function returns True.
        """

        self._recipes.modify_recipe(
            self._user[0], self._chosen_recipe[2], instructions)

        return bool(self._chosen_recipe)

    def delete_chosen_recipe(self):
        """Deletes the row that matches _chosen_recipe in SQL data table recipes.

        Returns:
            boolean: A boolean that informs whether or not the recipe was successfully deleted.
            If _chosen_recipe is None, nothing could be deleted, and the function returns False.
            If _chosen_recipe is not None, function delete_recipe() is able to find matching row
            from data table recipes and delete it. Thus the function returns True.
        """

        self._recipes.delete_recipe(self._user[0], self._chosen_recipe[2])

        return bool(self._chosen_recipe)


cookbookapp_functions = CookbookAppFunctions()
