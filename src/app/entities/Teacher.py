from uuid import uuid4
from datetime import datetime
from dataclasses import dataclass

from .props import TeacherProps
from src.shared.src.logic import Result
from src.shared.src.domain import Entity


@dataclass
class TeacherPropsResult(TeacherProps):
    id: str


class Teacher:
    class __private(Entity[TeacherProps]):
        def __init__(self, props: TeacherProps, id: str = None):
            super().__init__(props, id)

    @classmethod
    def create(cls, props: TeacherProps, id: str = None):
        """Create a teacher entity"""

        if not id:
            id = uuid4()

        props.created_at = datetime.utcnow
        props.updated_at = datetime.utcnow

        teacher = cls.__private(props, id)

        return Result.ok(
            TeacherPropsResult(
                id=teacher.id,
                user_id=teacher.props.user_id,
                created_at=teacher.props.created_at,
                updated_at=teacher.props.updated_at,
            )
        )
