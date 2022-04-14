from uuid import uuid4
from dataclasses import dataclass

from .props import ContactProps
from src.shared.src.logic import Result
from src.shared.src.domain import Entity


@dataclass
class ContactPropsResult(ContactProps):
    id: str


class Contact:
    class __private(Entity[ContactProps]):
        def __init__(self, props: ContactProps, id: str = None):
            super().__init__(props, id)

    @classmethod
    def create(cls, props: ContactProps, id: str = None):
        """Create a contact entity"""

        if not id:
            id = uuid4()

        contact = cls.__private(props, id)

        return Result.ok(
            ContactPropsResult(
                id=contact.id, phone=contact.props.phone, user_id=contact.props.user_id
            )
        )
