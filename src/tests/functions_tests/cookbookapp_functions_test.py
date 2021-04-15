import unittest
from functions.cookbookapp_functions import CookbookAppFunctions


class FakeUserDatabase:
    def __init__(self):
        self._users = []

    def search_user(self, username):
        for user in self._users:
            if user[1] == username:
                return user
        return None

    def add_user(self, username):
        user_exists = self.search_user(username)

        if user_exists:
            return False
        else:
            id = len(self._users)+1
            self._users.append((id, username))
            return True

    def erase_all_users(self):
        self._users = []


class FakeRecipesDatabase:
    def __init__(self):
        self._recipes = []

    def search_recipe(self, user_id, name):
        for recipe in self._recipes:
            if recipe[1] == user_id and recipe[2] == name:
                return recipe
        return None

    def add_recipe(self, user_id, name, instructions):
        id = len(self._recipes)+1
        self._recipes.append((id, user_id, name, instructions))

    def search_users_recipes(self, user_id):
        returns = []
        for recipe in self._recipes:
            if recipe[1] == user_id:
                returns.append(recipe)

        if returns != []:
            return returns
        return None

    def erase_all_recipes(self):
        self._recipes = []


class TestCookBookAppFunctions(unittest.TestCase):
    def setUp(self):
        self.fakeuserdatabase = FakeUserDatabase()
        self.fakerecipesdatabase = FakeRecipesDatabase()
        self.cookbookapp_functions = CookbookAppFunctions(
            self.fakeuserdatabase, self.fakerecipesdatabase)
        self.fakeuserdatabase.add_user("Leon")
        self.fakeuserdatabase.add_user("Stansfield")
        self.fakerecipesdatabase.add_recipe(
            1, "Sandwich", "Take a bread and butter it.")
        self.fakerecipesdatabase.add_recipe(
            1, "Glass of milk", "Pour milk in glass.")
        self.fakerecipesdatabase.add_recipe(2, "Pickles", "Pickles")

    def test_log_in_works_with_existing_user_correctly(self):
        returns = self.cookbookapp_functions.log_in("Leon")
        self.assertEqual(returns, True)

    def test_log_in_works_with_nonexisting_user_correctly(self):
        returns = self.cookbookapp_functions.log_in("Tony")
        self.assertEqual(returns, False)

    def test_log_out_works_correctly(self):
        returns = self.cookbookapp_functions.log_out()
        self.assertEqual(returns, True)

    def test_sign_in_works_correctly_with_previously_nonexistent_user(self):
        returns = self.cookbookapp_functions.sign_in("Mathilda")
        self.assertEqual(returns, True)

    def test_sign_in_works_correctly_with_existent_user(self):
        returns = self.cookbookapp_functions.sign_in("Leon")
        self.assertEqual(returns, False)

    def test_current_user_works_correctly_with_default(self):
        returns = self.cookbookapp_functions.current_user()
        self.assertEqual(returns, None)

    def test_current_user_works_correctly_with_logged_in_user(self):
        self.cookbookapp_functions.log_in("Leon")
        returns = self.cookbookapp_functions.current_user()
        self.assertEqual(returns, (1, "Leon"))

    def test_users_recipes_returns_recipes_correctly_when_logged_in(self):
        self.cookbookapp_functions.log_in("Leon")
        returns = self.cookbookapp_functions.users_recipes()
        self.assertEqual(returns, [(1, 1, "Sandwich", "Take a bread and butter it."), (
            2, 1, "Glass of milk", "Pour milk in glass.")])

    def test_add_recipes_returns_True_correctly_when_logged_in(self):
        self.cookbookapp_functions.log_in("Stansfield")
        returns = self.cookbookapp_functions.add_recipes(
            "Chinese", "Order chinese food")
        self.assertEqual(returns, True)

    def test_set_chosen_recipe_returns_True_with_existing_recipe(self):
        self.cookbookapp_functions.log_in("Leon")
        returns = self.cookbookapp_functions.set_chosen_recipe("Glass of milk")
        self.assertEqual(returns, True)

    def test_set_chosen_recipe_returns_False_with_nonexisting_recipe(self):
        self.cookbookapp_functions.log_in("Leon")
        returns = self.cookbookapp_functions.set_chosen_recipe("Cake")
        self.assertEqual(returns, False)

    def test_get_chosen_recipe_default_is_None(self):
        returns = self.cookbookapp_functions.get_chosen_recipe()
        self.assertEqual(returns, None)

    def test_get_chosen_recipe_returns_recipe(self):
        self.cookbookapp_functions.log_in("Leon")
        self.cookbookapp_functions.set_chosen_recipe("Glass of milk")
        returns = self.cookbookapp_functions.get_chosen_recipe()
        self.assertEqual(
            returns, (2, 1, "Glass of milk", "Pour milk in glass."))

    def test_no_chosen_recipe_returns_True(self):
        returns = self.cookbookapp_functions.no_chosen_recipe()
        self.assertEqual(returns, True)
