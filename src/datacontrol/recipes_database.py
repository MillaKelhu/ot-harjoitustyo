import sqlite3

class RecipesDatabase:
    def __init__(self):
        self._db = sqlite3.connect("recipes.db")
        self._db.isolation_level = None

        self._table_Recipes_exists()

    def _table_Recipes_exists(self):
        self._db.execute("CREATE TABLE IF NOT EXISTS Recipes (id INTEGER PRIMARY KEY, user_id INTEGER, name TEXT, instructions TEXT)")

    def search_recipe(self, user_id, name):
        recipe = self._db.execute("SELECT * FROM Recipes WHERE user_id=? AND name=?", [user_id, name]).fetchone()

        return recipe

    def add_recipe(self, user_id, name, instructions):
        recipe_exists = self.search_recipe(user_id, name)

        if recipe_exists is not None:
            return False
        else:
            self._db.execute("INSERT INTO Recipes (user_id, name, instructions) VALUES (?, ?, ?)", [user_id, name, instructions])
            return True

    def search_users_recipes(self, user_id):
        recipes = self._db.execute("SELECT * FROM Recipes WHERE user_id=?", [user_id]).fetchall()

        if recipes != []:
            return recipes
        return None

    def erase_all_recipes(self):
        self._db.execute("DROP TABLE Recipes")   
        self._table_Recipes_exists()   

recipes_database = RecipesDatabase()