from unittest import TestCase

from src.app.handlers import DeleteUserHandler

from src.app.repositories import UserRepository


class TestUserHandler(TestCase):
    def test_delete_user_handler(self):

        delete_handle = DeleteUserHandler(UserRepository)

        result = delete_handle.handle(user_id="871f96e8-6a12-4383-822e-791794f4798d")
        print(result)

        self.assertEqual(result.error_value(), None)
