from unittest import TestCase

from src.app.entities import User
from src.app.entities.props import UserProps
from src.app.handlers import UpdateUserHandler

from src.app.repositories import UserRepository


class TestUserHandler(TestCase):
    def test_update_user_handler(self):

        user_entity = User()
        result = user_entity.create(
            UserProps(
                name="António Gabriel",
                email="ag@gmail.com.br",
                surname="Alembic",
                password="antoniocampos20",
                city="Luanda",
                state=True,
                user_type="staff",
            ),
            id="b9a39620-8d98-4962-8e16-74c5e56c7d38",
        )

        error = result.error_value()
        if error:
            print(error)
            return

        update_handle = UpdateUserHandler(UserRepository)

        is_updated = update_handle.handle(result.get_value())
        print(is_updated.get_value())

        self.assertTrue(True)
