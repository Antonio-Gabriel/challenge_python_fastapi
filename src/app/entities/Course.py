from uuid import uuid4
from datetime import datetime
from dataclasses import dataclass

from .props import CourseProps
from src.shared.src.domain import Entity
from src.shared.src.logic import Result, Guard


@dataclass
class CoursePropsResult(CourseProps):
    id: str


class Course:
    class __private(Entity[CourseProps]):
        def __init__(self, props: CourseProps, id: str = None):
            super().__init__(props, id)

    @classmethod
    def create(cls, props: CourseProps, id: str = None):
        """Create a course entity"""

        if not id:
            id = uuid4()

        props.created_at = datetime.utcnow
        props.updated_at = datetime.utcnow

        guard_result = Guard.against_null_or_empty(props.name)

        if guard_result is not None and not guard_result.succeeded:
            return Result.fail(guard_result.message)

        course = cls.__private(props, id)

        return Result.ok(
            CoursePropsResult(
                id=course.id,
                name=course.props.name,
                state=course.props.state,
                endDate=course.props.endDate,
                startDate=course.props.startDate,
                teacher_id=course.props.teacher_id,
                created_at=course.props.created_at,
                updated_at=course.props.updated_at,
            )
        )
