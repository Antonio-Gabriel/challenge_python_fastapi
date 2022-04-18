from ..entities.props import CourseProps
from ..interfaces import ICourseRepository

from ..sql import CourseModel, TeacherModel, UserModel
from ..config import session_maker


class CourseRepository(ICourseRepository):
    def save(entity: CourseProps):
        """save entity into db"""

        course = CourseModel(
            name=entity.name,
            startDate=entity.startDate,
            endDate=entity.endDate,
            state=entity.state,
            teacher_id=entity.teacher_id,
        )

        with session_maker() as session:
            session.add(course)
            session.commit()

        return course

    def update(entity: CourseProps):
        """update entity into db"""
        with session_maker() as session:
            course = (
                session.query(CourseModel)
                .filter(CourseModel.id == entity.id)
                .update(
                    {
                        CourseModel.name: entity.name,
                        CourseModel.startDate: entity.startDate,
                        CourseModel.endDate: entity.endDate,
                        CourseModel.state: entity.state,
                        CourseModel.teacher_id: entity.teacher_id,
                    }
                )
            )

            session.commit()
        return course

    def get():
        """get all entities"""
        with session_maker() as session:
            courses = session.query(CourseModel).values(
                CourseModel.id,
                CourseModel.name,
                CourseModel.startDate,
                CourseModel.endDate,
                CourseModel.state,
                CourseModel.teacher_id,
            )

            result_set = set()
            resultList = []
            for course in courses:
                if course.name not in result_set:
                    teacher = (
                        session.query(TeacherModel)
                        .filter(
                            TeacherModel.id == course.teacher_id,
                            UserModel.id == TeacherModel.user_id,
                        )
                        .values(
                            TeacherModel.id,
                            UserModel.name,
                            UserModel.email,
                        )
                    )

                    teacher_list = []
                    for current_teacher in teacher:
                        teacher_list.append(
                            {
                                "id": current_teacher.id,
                                "name": current_teacher.name,
                                "email": current_teacher.email,
                            }
                        )

                    resultList.append(
                        {
                            "id": course.id,
                            "name": course.name,
                            "startDate": course.startDate,
                            "endDate": course.endDate,
                            "state": course.state,
                            "teacher": {
                                "id": teacher_list[0]["id"],
                                "name": teacher_list[0]["name"],
                                "email": teacher_list[0]["email"],
                            },
                        }
                    )

                    result_set.add(course.name)

        return resultList

    def get_by_teacher_id(entity_id: str):
        """get entity by teacher id"""

        with session_maker() as session:
            courses = (
                session.query(CourseModel)
                .filter(CourseModel.teacher_id == entity_id)
                .values(
                    CourseModel.id,
                    CourseModel.name,
                    CourseModel.startDate,
                    CourseModel.endDate,
                    CourseModel.state,
                    CourseModel.teacher_id,
                )
            )

            result_set = set()
            resultList = []
            for course in courses:
                if course.name not in result_set:
                    teacher = (
                        session.query(TeacherModel)
                        .filter(
                            TeacherModel.id == course.teacher_id,
                            UserModel.id == TeacherModel.user_id,
                        )
                        .values(
                            TeacherModel.id,
                            UserModel.name,
                            UserModel.email,
                        )
                    )

                    teacher_list = []
                    for current_teacher in teacher:
                        teacher_list.append(
                            {
                                "id": current_teacher.id,
                                "name": current_teacher.name,
                                "email": current_teacher.email,
                            }
                        )

                    resultList.append(
                        {
                            "id": course.id,
                            "name": course.name,
                            "startDate": course.startDate,
                            "endDate": course.endDate,
                            "state": course.state,
                            "teacher": {
                                "id": teacher_list[0]["id"],
                                "name": teacher_list[0]["name"],
                                "email": teacher_list[0]["email"],
                            },
                        }
                    )

                    result_set.add(course.name)

        return resultList

    def get_by_registed_course(entity_id: str, course_name: str):
        """get entity by id and course name"""
        with session_maker() as session:
            user = (
                session.query(CourseModel)
                .filter(
                    CourseModel.teacher_id == entity_id, CourseModel.name == course_name
                )
                .first()
            )

        return user

    def get_by_id(entity_id: str):
        """get entity by id and course name"""
        with session_maker() as session:
            user = (
                session.query(TeacherModel).filter(TeacherModel.id == entity_id).first()
            )

        return user

    def delete(entity_id: str):
        """delete entity into db"""
        with session_maker() as session:
            user = (
                session.query(CourseModel).filter(CourseModel.id == entity_id).delete()
            )

            session.commit()

        return user
