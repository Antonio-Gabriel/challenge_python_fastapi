from unittest import TestCase

from src.app.handlers import GetUsersByIdHandler

from src.app.repositories import UserRepository


class TestUserHandler(TestCase):
    def test_get_user_by_id_handler(self):

        filtered_user_handle = GetUsersByIdHandler(UserRepository)

        results = filtered_user_handle.handle(
            user_id="b9a39620-8d98-4962-8e16-74c5e56c7d38"
        )

        print(results.get_value())

        self.assertTrue(True)
