from src.app.entities import Teacher
from src.app.entities.props import TeacherProps


class TeacherAdapter:
    @staticmethod
    def create(
        user_id: str,
        id: str = False,
    ):
        teacher_entity = Teacher()
        teacher_result = teacher_entity.create(
            TeacherProps(user_id=user_id),
            id=id,
        )

        return teacher_result
