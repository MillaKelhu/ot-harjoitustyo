import unittest
from datacontrol.users_database import user_database


class TestUserDatabase(unittest.TestCase):
    def setUp(self):
        user_database.erase_all_users()
        user_database.add_user("Adam")

    def test_search_user_finds_existing_user_correctly(self):
        returns = user_database.search_user("Adam")
        self.assertEqual(returns, (1, "Adam"))

    def test_search_nonexistent_user_returns_None_correctly(self):
        returns = user_database.search_user("Eve")
        self.assertEqual(returns, None)

    def test_add_user_adds_previously_nonexistent_user_correctly(self):
        returns = user_database.add_user("Eve")
        self.assertEqual(returns, True)

    def test_add_user_prevents_user_duplicates(self):
        returns = user_database.add_user("Adam")
        self.assertEqual(returns, False)
