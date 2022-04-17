from typing import Type

from ...entities.props import UserProps, TeacherProps
from ...interfaces import IUserRepository, ITeacherRepository

from ..user.CreateUserHandler import CreateUserHandler
from ...utils.CheckDuplicatesItemsInList import checkDuplicatesItemsInList

from src.shared.src.logic import Result


class CreateTeacherHandler:
    def __init__(
        self,
        user_repository: Type[IUserRepository],
        teacher_repository: Type[ITeacherRepository],
    ) -> None:
        self.__user_repository = user_repository
        self.__teacher_repository = teacher_repository

    def handle(
        self, requestDTO: UserProps, secondeRequestDTO: TeacherProps, contacts: list
    ) -> Result[UserProps]:

        user_handler = CreateUserHandler(self.__user_repository)
        user_base = user_handler.handle(requestDTO)

        error = user_base.error_value()

        if error:
            return Result.fail(user_base.error_value())

        verifycontacts = checkDuplicatesItemsInList(contacts)

        if verifycontacts:
            return Result.fail("Do you have duplicated contacts!")

        statement = self.__teacher_repository.save(secondeRequestDTO)

        self.__teacher_repository.register_contacts(contacts, secondeRequestDTO.user_id)

        if statement:
            return Result.ok(UserProps)
