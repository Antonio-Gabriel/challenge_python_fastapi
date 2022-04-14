from typing import Type

from ...entities.props import UserProps
from ...interfaces import IUserRepository

from src.shared.src.logic import Result
from .EmailAlreadyExists import EmailAlreadyExists


class UpdateUserHandler:
    def __init__(self, user_repository: Type[IUserRepository]) -> None:
        self.__user_repository = user_repository

    def handle(self, requestDTO: UserProps) -> Result[UserProps]:

        get_user = self.__user_repository.get_by_id(requestDTO.id)

        if get_user.email != requestDTO.email:
            email_already_exists = self.__user_repository.get_by_email(requestDTO.email)

            if email_already_exists:
                return EmailAlreadyExists(requestDTO.email)

        statement = self.__user_repository.update(requestDTO)

        if statement:
            return Result.ok("Successfully user updated!")
