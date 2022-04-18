from src.app.entities import Enrollment
from src.app.entities.props import EnrollmentProps


class EnrollmentAdapter:
    @staticmethod
    def create(
        student_id: int,
        course_id: int,
        id: str = False,
    ):
        enrollment_entity = Enrollment()
        teacher_result = enrollment_entity.create(
            EnrollmentProps(
                student_id=student_id, course_id=course_id, created_at="", updated_at=""
            ),
            id=id,
        )

        return teacher_result
