from uuid import uuid4
from datetime import datetime
from dataclasses import dataclass

from .props import EnrollmentProps
from src.shared.src.logic import Result
from src.shared.src.domain import Entity


@dataclass
class EnrollmentPropsResult(EnrollmentProps):
    id: str


class Enrollment:
    class __private(Entity[EnrollmentProps]):
        def __init__(self, props: EnrollmentProps, id: str = None):
            super().__init__(props, id)

    @classmethod
    def create(cls, props: EnrollmentProps, id: str = None):
        """Create a enrollment entity"""

        if not id:
            id = uuid4()

        props.created_at = datetime.utcnow
        props.updated_at = datetime.utcnow

        enrollment = cls.__private(props, id)

        return Result.ok(
            EnrollmentPropsResult(
                id=enrollment.id,
                course_id=enrollment.props.course_id,
                student_id=enrollment.props.student_id,
                created_at=enrollment.props.created_at,
                updated_at=enrollment.props.updated_at,
            )
        )
