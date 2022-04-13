from unittest import TestCase

from src.app.entities import User
from src.app.entities.props import UserProps


class TestUserEntity(TestCase):
    def test_user_entity_base(self):

        user_entity = User()
        result = user_entity.create(
            UserProps(
                name="António Campos Gabriel",
                email="ag@gmail.com.br",
                surname="Gabriel",
                password="antoniocampos20",
                city="",
                state=True,
                user_type="teacher",
            )
        )

        error = result.error_value()
        if error:
            print(error)
            return

        print(result.get_value())

        self.assertTrue(result.IS_SUCCESS)
