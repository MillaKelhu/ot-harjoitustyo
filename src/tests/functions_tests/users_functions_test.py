import unittest
from functions.user_functions import user_functions
from datacontrol.users_database import user_database

class TestUserFunctions(unittest.TestCase):
    def setUp(self):
        user_database.erase_all_users()
        user_database.add_user("Adam")

    def test_log_in_works_with_existing_user_correctly(self):
        returns = user_functions.log_in("Adam")
        self.assertEqual(returns, True)

    def test_log_in_works_with_nonexisting_user_correctly(self):
        returns = user_functions.log_in("Lilith")
        self.assertEqual(returns, False)

    def test_log_out_works_correctly(self):
        returns = user_functions.log_out()
        self.assertEqual(returns, True)

    def test_sign_in_works_correctly_with_previously_nonexistent_user(self):
        returns = user_functions.sign_in("Eve")
        self.assertEqual(returns, True)

    def test_sign_in_works_correctly_with_existent_user(self):
        returns = user_functions.sign_in("Adam")
        self.assertEqual(returns, False)

    def test_current_user_works_correctly_with_default(self):
        returns = user_functions.current_user()
        self.assertEqual(returns, None)

    def test_current_user_works_correctly_with_logged_in_user(self):
        user_functions.log_in("Adam")
        returns = user_functions.current_user()
        self.assertEqual(returns, "Adam")
    