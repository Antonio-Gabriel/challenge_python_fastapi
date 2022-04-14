from uuid import uuid4
from datetime import datetime
from dataclasses import dataclass

from .props import StudentProps
from src.shared.src.logic import Result
from src.shared.src.domain import Entity


@dataclass
class StudentPropsResult(StudentProps):
    id: str


class Student:
    class __private(Entity[StudentProps]):
        def __init__(self, props: StudentProps, id: str = None):
            super().__init__(props, id)

    @classmethod
    def create(cls, props: StudentProps, id: str = None):
        """Create a student entity"""

        if not id:
            id = uuid4()

        props.created_at = datetime.utcnow
        props.updated_at = datetime.utcnow

        student = cls.__private(props, id)

        return Result.ok(
            StudentPropsResult(
                id=student.id,
                user_id=student.props.user_id,
                created_at=student.props.created_at,
                updated_at=student.props.updated_at,
            )
        )
