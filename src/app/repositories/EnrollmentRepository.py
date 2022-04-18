from ..interfaces import IEnrollmentRepository
from ..entities.props import EnrollmentProps

from ..config import session_maker
from ..sql import EnrollmentModel


class EnrollmentRepository(IEnrollmentRepository):
    def register(entity: EnrollmentProps):
        """register entity into db"""
        enrollment = EnrollmentModel(
            student_id=entity.student_id, course_id=entity.course_id
        )

        with session_maker() as session:
            session.add(enrollment)
            session.commit()

        return enrollment

    def get_registered_student(student_id: int, course_id: int):
        """get registered entity into db"""

        with session_maker() as session:
            enrollment = (
                session.query(EnrollmentModel)
                .filter(
                    EnrollmentModel.student_id == student_id,
                    EnrollmentModel.course_id == course_id,
                )
                .first()
            )

        return enrollment
