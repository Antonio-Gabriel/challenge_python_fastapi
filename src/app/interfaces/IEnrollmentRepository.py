from abc import ABC, abstractmethod

from ..entities.props import EnrollmentProps


class IEnrollmentRepository(ABC):
    @abstractmethod
    def register(entity: EnrollmentProps):
        """register entity into db"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_registered_student(student_id: int, course_id: int):
        """get registered entity into db"""

        raise NotImplementedError("Method not implemented")
