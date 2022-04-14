from unittest import TestCase

from src.app.entities import User
from src.app.entities.props import UserProps
from src.app.handlers import CreateUserHandler

from src.app.repositories import UserRepository


class TestUserHandler(TestCase):
    def test_create_user_handler(self):

        user_entity = User()
        result = user_entity.create(
            UserProps(
                name="António Gabriel",
                email="ag@gmail.com.br",
                surname="Alembic",
                password="antoniocampos20",
                city="Luanda",
                user_type="staff",
            )
        )

        error = result.error_value()
        if error:
            print(error)
            return

        create_handle = CreateUserHandler(UserRepository)

        is_saved = create_handle.handle(result.get_value())
        print(is_saved.error_value())

        self.assertTrue(True)
