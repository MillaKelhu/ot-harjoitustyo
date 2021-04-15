import unittest
from datacontrol.recipes_database import recipes_database


class TestUserDatabase(unittest.TestCase):
    def setUp(self):
        recipes_database.erase_all_recipes()
        recipes_database.add_recipe(
            1, "Sandwich", "Take a bread and butter it.")
        recipes_database.add_recipe(1, "Glass of milk", "Pour milk in glass.")
        recipes_database.add_recipe(2, "Cocoa", "Mix cocoa powder with milk.")

    def test_search_recipe_finds_existing_recipe_correctly(self):
        returns = recipes_database.search_recipe(1, "Sandwich")
        self.assertEqual(returns, (1, 1, "Sandwich",
                         "Take a bread and butter it."))

    def test_search_recipe_nonexistent_recipe_returns_None(self):
        returns = recipes_database.search_recipe(1, "Salad")
        self.assertEqual(returns, None)

    def test_search_recipe_nonexistent_user_returns_None(self):
        returns = recipes_database.search_recipe(3, "Cocoa")
        self.assertEqual(returns, None)

    def test_add_recipe_adds_previously_nonexistent_recipe_correctly(self):
        returns = recipes_database.add_recipe(
            2, "Salad", "Wash a salad and put its leaves in a bowl.")
        self.assertEqual(returns, True)

    def test_add_recipe_prevents_duplicates(self):
        returns = recipes_database.add_recipe(
            1, "Sandwich", "Take a bread, butter it, and put a slice of cheese on it.")
        self.assertEqual(returns, False)

    def test_search_users_recipes_returns_recipes_correctly(self):
        returns = recipes_database.search_users_recipes(1)
        self.assertEqual(returns, [(1, 1, "Sandwich", "Take a bread and butter it."), (
            2, 1, "Glass of milk", "Pour milk in glass.")])

    def test_search_users_recipes_returns_nonexistent_users_recipes_as_None(self):
        returns = recipes_database.search_users_recipes(3)
        self.assertEqual(returns, None)
