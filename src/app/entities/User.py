from uuid import uuid4
from dataclasses import dataclass

from .props import UserProps
from src.shared.src.domain import Entity
from src.shared.src.logic import Result, Guard

from .enums.Users import Users
from .validators import Email, PasswordHash


@dataclass
class UserPropsResult(UserProps):
    id: str


class User:
    class __private(Entity[UserProps]):
        def __init__(self, props: UserProps, id: str = None):
            super().__init__(props, id)

    @classmethod
    def create(cls, props: UserProps, id: str = None):
        """Create a user entity"""

        if not id:
            id = uuid4()

        guard_result = Guard.against_null_or_empty_bulk(
            **{
                "name": props.name,
                "email": props.email,
                "surname": props.surname,
                "password": props.password,
            }
        )

        if not props.user_type:
            return Result.fail("Please insert a valid user type!")

        try:
            if Users._member_map_[props.user_type]:
                pass
        except:
            return Result.fail("Invalid user type!, try [Staff, teacher, student]")

        if guard_result is not None and not guard_result.succeeded:
            return Result.fail(guard_result.message)

        if not Email.is_valid(props.email):
            return Result.fail("Invalid email address, pleace check your email!")

        props.password = props.password = cls.__password_encrypt(props.password)

        user = cls.__private(props, id)

        return Result.ok(
            UserPropsResult(
                id=user.id,
                name=user.props.name,
                email=user.props.email,
                surname=user.props.surname,
                password=user.props.password,
                city=user.props.city,
                state=user.props.state,
                user_type=user.props.user_type,
            )
        )

    @classmethod
    def __password_encrypt(cls, password) -> bytes:
        """Enctrypt password"""

        return PasswordHash.encrypt(password)

    @classmethod
    def compare(cls, hash_pass: str, comparison_pass: bytes) -> bool:
        """Verify if password iblacks valid or not"""

        if hash_pass and comparison_pass:

            return PasswordHash.compare(hash_pass, comparison_pass)

        return Result.fail("Complete the parameters to compare passwords")
