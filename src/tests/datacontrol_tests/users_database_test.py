import unittest
from datacontrol.users_database import user_database


class TestUserDatabase(unittest.TestCase):
    def setUp(self):
        user_database.erase_all_users()
        user_database.add_user("Adam", "123")

    def test_search_user_finds_existing_user_correctly_without_password(self):
        returns = user_database.search_user("Adam")
        self.assertEqual(returns, (1, "Adam", "123"))

    def test_search_user_finds_existing_user_correctly_with_password(self):
        returns = user_database.search_user("Adam", "123")
        self.assertEqual(returns, (1, "Adam", "123"))

    def test_search_user_returns_None_with_wrong_password(self):
        returns = user_database.search_user("Adam", "456")
        self.assertEqual(returns, None)

    def test_search_nonexistent_user_returns_None_correctly(self):
        returns = user_database.search_user("Eve")
        self.assertEqual(returns, None)

    def test_add_user_adds_previously_nonexistent_user_correctly(self):
        returns = user_database.add_user("Eve", "123")
        self.assertEqual(returns, True)

    def test_add_user_prevents_username_duplicates(self):
        returns = user_database.add_user("Adam", "456")
        self.assertEqual(returns, False)

    def test_get_all_users_works_correctly(self):
        users = user_database.get_all_users()

        self.assertEqual(users, [(1, "Adam", "123")])

    def test_erase_all_users_works_correctly(self):
        user_database.erase_all_users()
        users = user_database.get_all_users()

        self.assertEqual(users, None)

    def test_search_user_returns_none_with_wrong_password(self):
        returns = user_database.search_user("Adam", "456")
        self.assertEqual(returns, None)
