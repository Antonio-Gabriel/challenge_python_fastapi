from datetime import datetime
from src.app.entities import Course
from src.app.entities.props import CourseProps


class CourseAdapter:
    @staticmethod
    def create(
        name: str,
        startDate: datetime,
        endDate: datetime,
        state: bool,
        teacher_id: int,
        id: str = False,
    ):
        course_entity = Course()
        course_result = course_entity.create(
            CourseProps(
                name=name,
                startDate=startDate,
                endDate=endDate,
                state=state,
                teacher_id=teacher_id,
                created_at="",
                updated_at="",
            ),
            id=id,
        )

        return course_result
