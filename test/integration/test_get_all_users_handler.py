from unittest import TestCase

from src.app.handlers import GetAllUserHandlers

from src.app.repositories import UserRepository


class TestUserHandler(TestCase):
    def test_get_all_users_handler(self):

        filtered_user_handle = GetAllUserHandlers(UserRepository)

        results = filtered_user_handle.handle()

        print(results.get_value()[0])

        self.assertTrue(True)
