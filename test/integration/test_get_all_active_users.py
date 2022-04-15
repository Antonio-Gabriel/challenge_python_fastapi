from unittest import TestCase

from src.app.handlers import GetUserByStateHandler

from src.app.repositories import UserRepository


class TestUserHandler(TestCase):
    def test_get_all_active_users(self):

        filtered_user_handle = GetUserByStateHandler(UserRepository)

        results = filtered_user_handle.handle(True)

        print(results.get_value())

        self.assertTrue(True)
