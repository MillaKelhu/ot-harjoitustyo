from database_connection import get_database_connection


class RecipesDatabase:
    def __init__(self, connection):
        self._db = connection
        self._db.isolation_level = None

    def search_recipe(self, user_id, name):
        recipe = self._db.execute(
            "SELECT * FROM recipes WHERE user_id=? AND name=?", [user_id, name]).fetchone()

        return recipe

    def add_recipe(self, user_id, name, instructions):
        recipe_exists = self.search_recipe(user_id, name)

        if recipe_exists is None:
            self._db.execute("INSERT INTO recipes (user_id, name, instructions) VALUES (?, ?, ?)", [
                             user_id, name, instructions])

        return not bool(recipe_exists)

    def search_users_recipes(self, user_id):
        recipes = self._db.execute(
            "SELECT * FROM recipes WHERE user_id=?", [user_id]).fetchall()

        if recipes != []:
            return recipes
        return None

    def erase_all_recipes(self):
        cursor = self._db.cursor()

        cursor.execute("DELETE FROM recipes")

        self._db.commit()

    def get_all_recipes(self):
        recipes = self._db.execute(
            "SELECT * FROM recipes").fetchall()

        if recipes == []:
            recipes = None

        return recipes

    def modify_recipe(self, user_id, name, new_instructions):
        recipe = self.search_recipe(user_id, name)

        if recipe:
            self._db.execute("UPDATE recipes SET instructions=? WHERE user_id=? AND name=?", [
                             new_instructions, user_id, name])

            recipe = self.search_recipe(user_id, name)

        return recipe

    def delete_recipe(self, user_id, name):
        recipe = self.search_recipe(user_id, name)

        if recipe:
            self._db.execute("DELETE FROM recipes WHERE user_id=? AND name=?", [
                user_id, name])

        return bool(recipe)


recipes_database = RecipesDatabase(get_database_connection())
