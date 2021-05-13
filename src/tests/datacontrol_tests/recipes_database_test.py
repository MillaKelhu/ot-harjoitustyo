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

    def test_add_recipe_adds_previously_nonexistent_recipe_correctly(self):
        returns = recipes_database.add_recipe(
            2, "Salad", "Wash a salad and put its leaves in a bowl.")
        self.assertEqual(returns, True)

    def test_add_recipe_users_can_add_same_recipes(self):
        returns = recipes_database.add_recipe(
            2, "Sandwich", "Take a bread and butter it.")
        self.assertEqual(returns, True)

    def test_add_recipe_prevents_duplicate_names(self):
        returns = recipes_database.add_recipe(
            1, "Sandwich", "Take a bread, butter it, and put a slice of cheese on it.")
        self.assertEqual(returns, False)

    def test_search_users_recipes_returns_recipes_correctly(self):
        returns = recipes_database.search_users_recipes(1)
        self.assertEqual(returns, [(1, 1, "Sandwich", "Take a bread and butter it."), (
            2, 1, "Glass of milk", "Pour milk in glass.")])

    def test_search_users_recipe_with_keyword_finds_recipes_correctly(self):
        returns = recipes_database.search_users_recipes(1, "bread")
        self.assertEqual(returns, [(1, 1, "Sandwich",
                         "Take a bread and butter it.")])

    def test_search_users_recipe_returns_None_with_nonexistent_keyword(self):
        returns = recipes_database.search_users_recipes(1, "salad")
        self.assertEqual(returns, None)

    def test_get_all_recipes_works_correctly(self):
        recipes = recipes_database.get_all_recipes()

        self.assertEqual(recipes, [(1, 1, "Sandwich", "Take a bread and butter it."), (
            2, 1, "Glass of milk", "Pour milk in glass."), (3, 2, "Cocoa", "Mix cocoa powder with milk.")])

    def test_erase_all_recipes_works_correctly(self):
        recipes_database.erase_all_recipes()
        recipes = recipes_database.get_all_recipes()

        self.assertEqual(recipes, None)

    def test_modify_recipe_works_correctly(self):
        returns = recipes_database.modify_recipe(
            1, "Sandwich", "Take a bread and put some jam and peanut butter on it.")

        self.assertEqual(returns, (1, 1, "Sandwich",
                         "Take a bread and put some jam and peanut butter on it."))

    def test_modify_recipe_returns_None_with_nonexisting_recipe(self):
        returns = recipes_database.modify_recipe(
            1, "Noodles", "Put on some cup noodles")

        self.assertEqual(returns, None)

    def test_delete_recipe_works_correctly(self):
        returns = recipes_database.delete_recipe(1, "Sandwich")

        self.assertEqual(returns, True)
