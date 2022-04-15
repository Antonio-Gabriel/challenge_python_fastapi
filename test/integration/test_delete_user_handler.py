from unittest import TestCase

from src.app.handlers import DeleteUserHandler

from src.app.repositories import UserRepository


class TestUserHandler(TestCase):
    def test_delete_user_handler(self):

        delete_handle = DeleteUserHandler(UserRepository)

        result = delete_handle.handle(user_id="b217b21a-7bb2-4b9d-a724-b07585259822")
        print(result.get_value())

        self.assertEqual(result.error_value(), None)
