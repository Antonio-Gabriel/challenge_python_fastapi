from typing import Type

from ...interfaces import IUserRepository

from src.shared.src.logic import Result


class GetAllUserHandlers:
    def __init__(self, user_repository: Type[IUserRepository]) -> None:
        self.__user_repository = user_repository

    def handle(self) -> Result[list]:

        users = self.__user_repository.get()

        return Result.ok(users)
