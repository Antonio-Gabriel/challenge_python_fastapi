from src.app.entities import User
from src.app.entities.props import UserProps


class UserAdapter:
    @staticmethod
    def create(
        name: str,
        email: str,
        surname: str,
        password: str,
        city: str,
        state: bool,
        user_type: str,
        id: str = False,
    ):
        user_entity = User()
        user_result = user_entity.create(
            UserProps(
                name=name,
                email=email,
                surname=surname,
                password=password,
                city=city,
                state=state,
                user_type=user_type,
            ),
            id=id,
        )

        return user_result
