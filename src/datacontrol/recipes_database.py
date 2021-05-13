from database_connection import get_database_connection


class RecipesDatabase:
    """Class that oversees and controls the SQL-database in which all recipes are saved.

    Attributes:
        _db: Connection to SQL-database.
    """

    def __init__(self, connection):
        """Constructor of class that establishes the connection to SQL-database.

        Args:
            connection (Connection): Connection to SQL-database.
        """

        self._db = connection
        self._db.isolation_level = None

    def search_recipe(self, user_id, name):
        """Searches and returns a row that contains the given arguments from data table recipes.

        Args:
            user_id (integer): The id of user that added the recipe.
            name (string): The name of the recipe.

        Returns:
            tuple or None: Depending on the results of a query, the function returns:
            a tuple that contains the id of recipe, id of user that added the recipe,
            the recipe name, and instructions;
            None, if the table doesn't have a row containing the given arguments.
        """

        recipe = self._db.execute(
            "SELECT * FROM recipes WHERE user_id=? AND name=?", [user_id, name]).fetchone()

        return recipe

    def add_recipe(self, user_id, name, instructions):
        """Adds a row into data table recipes.

        Args:
            user_id (integer): The id of user that adds the recipe.
            name (string): The name of the recipe.
            instructions (string): Instructions of recipe.

        Returns:
            boolean: Variable recipe_exists contains the result of function search_recipe
            with the given arguments, and that is turned into a boolean.
            The function returns the opposite of this boolean, signifying whether or not a new row,
            and thus a recipe, was added successfully.
        """

        recipe_exists = self.search_recipe(user_id, name)

        if recipe_exists is None:
            self._db.execute("INSERT INTO recipes (user_id, name, instructions) VALUES (?, ?, ?)", [
                             user_id, name, instructions])

        return not bool(recipe_exists)

    def search_users_recipes(self, user_id, keyword=None):
        """Searches and returns rows that contain the given argument from data table recipes.

        Args:
            user_id (integer): The id of user that added the recipe(s).
            keyword (string, default None): A string variable used to filter the search results.
            If none are given, the query returns all user's recipes.

        Returns:
            list or None: Depending on the result of the query, the function returns:
            the rows as a list containing tuples;
            None, if the table has no rows with the given user id.
        """
        if keyword:
            keyword = f'%{keyword}%'

            recipes = self._db.execute(
                "SELECT * FROM recipes WHERE user_id=? AND LOWER(name) LIKE LOWER(?) OR LOWER(instructions) LIKE LOWER(?)", 
                [user_id, keyword, keyword]).fetchall()

        else:

            recipes = self._db.execute(
                "SELECT * FROM recipes WHERE user_id=?", [user_id]).fetchall()


        if recipes != []:
            return recipes
        return None

    def erase_all_recipes(self):
        """Deletes all rows from the data table recipes.
        """

        cursor = self._db.cursor()

        cursor.execute("DELETE FROM recipes")

        self._db.commit()

    def get_all_recipes(self):
        """Searches and returns all rows from data table recipes.

        Returns:
            list or None: Depending on the result of the query, the function returns:
            the rows as a list containing tuples;
            None, if the table is empty.
        """

        recipes = self._db.execute(
            "SELECT * FROM recipes").fetchall()

        if recipes == []:
            recipes = None

        return recipes

    def modify_recipe(self, user_id, name, new_instructions):
        """Replaces a single field in data table recipes, in column "instructions"
        on the row that contains the given user id and recipe name.

        Args:
            user_id (integer): The id of user that added the recipe.
            name (string): The name of the recipe.
            new_instructions (string): New instructions that replaces
            the row's "instructions" field's content.

        Returns:
            tuple or None: Depending on the result of the query, the function returns:
            a tuple containing the modified recipe;
            None, if the table has no row with the given user id and recipe name.
        """

        recipe = self.search_recipe(user_id, name)

        if recipe:
            self._db.execute("UPDATE recipes SET instructions=? WHERE user_id=? AND name=?", [
                             new_instructions, user_id, name])

            recipe = self.search_recipe(user_id, name)

        return recipe

    def delete_recipe(self, user_id, name):
        """Deletes a row contianing the given arguments in data table recipes.

        Args:
            user_id (integer): The id of user that added the recipe.
            name (string): The name of the recipe.

        Returns:
            boolean: A boolean that tells whether or not a row with given
            arguments exists in the table, and consequently whether or
            not it was removed successfully.
        """

        recipe = self.search_recipe(user_id, name)

        if recipe:
            self._db.execute("DELETE FROM recipes WHERE user_id=? AND name=?", [
                user_id, name])

        return bool(recipe)


recipes_database = RecipesDatabase(get_database_connection())
