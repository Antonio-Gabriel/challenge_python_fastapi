from typing import Type

from ...entities import User
from ...entities.props import UserProps
from ...interfaces import IUserRepository

from src.shared.src.logic import Result


class AuthUserHandler:
    def __init__(self, user_repository: Type[IUserRepository]) -> None:
        self.__user_repository = user_repository

    def handle(self, email: str, password: str) -> Result[UserProps]:

        email_already_exists = self.__user_repository.get_by_email(email)

        if not email_already_exists:
            return Result.fail("Invalid email or password!")

        if not User.compare(password, email_already_exists.password.encode()):
            return Result.fail("Invalid email or password!")

        return Result.ok(email_already_exists)
