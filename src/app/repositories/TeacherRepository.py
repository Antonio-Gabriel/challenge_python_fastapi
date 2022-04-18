from typing import List
from ..interfaces import ITeacherRepository
from ..entities.props import TeacherProps, ContactProps

from ..config import session_maker
from ..sql import (
    TeacherModel,
    CourseModel,
    EnrollmentModel,
    ContactModel,
    UserModel,
)


class TeacherRepository(ITeacherRepository):
    def save(entity: TeacherProps):
        """save entity into db"""

        teacher = TeacherModel(
            user_id=entity.user_id,
        )

        with session_maker() as session:
            session.add(teacher)
            session.commit()

        return teacher

    def register_contacts(*entity: List[ContactProps]):
        """save contacts into db"""
        contact_model = []
        for contact in entity[0]:
            contact_model.append(ContactModel(phone=contact, user_id=entity[1]))

        for teacher_contact in contact_model:
            with session_maker() as session:
                session.add(teacher_contact)
                session.commit()

        return teacher_contact

    def get():
        """Get all teachers"""
        with session_maker() as session:
            teachers = (
                session.query(TeacherModel)
                .filter(UserModel.user_type == "teacher")
                .values(
                    TeacherModel.id,
                    UserModel.name,
                    UserModel.surname,
                    UserModel.email,
                    UserModel.city,
                    UserModel.user_type,
                )
            )

            result_set = set()
            resultList = []
            for teacher in teachers:

                if teacher.name not in result_set:

                    teacher_contacts = (
                        session.query(ContactModel)
                        .filter(ContactModel.user_id == UserModel.id)
                        .all()
                    )

                    resultList.append(
                        {
                            "id": teacher.id,
                            "name": teacher.name,
                            "surname": teacher.surname,
                            "email": teacher.email,
                            "city": teacher.city,
                            "phone": teacher_contacts,
                            "user_type": teacher.user_type,
                        }
                    )

                    result_set.add(teacher.name)

        return resultList

    def get_teacher_courses(entity_id: int):
        """Get all courses of teacher"""
        with session_maker() as session:
            courses = (
                session.query(CourseModel)
                .filter(TeacherModel.id == entity_id)
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

            student_result_set = set()
            totalStudent = []
            for course in courses:
                if course.name not in result_set:

                    students = (
                        session.query(EnrollmentModel)
                        .filter(EnrollmentModel.course_id == course.id)
                        .all()
                    )

                    for student in students:
                        if student.id not in student_result_set:
                            totalStudent.append({"id": student.id})

                            student_result_set.add(student.id)

                    resultList.append(
                        {
                            "id": course.id,
                            "name": course.name,
                            "startDate": course.startDate,
                            "endDate": course.endDate,
                            "state": course.state,
                        }
                    )

                    result_set.add(course.name)

        return {"courses": resultList, "total_students": len(totalStudent)}

    def get_by_id(entity_id: str):
        """get entity by id"""
        with session_maker() as session:
            user = (
                session.query(UserModel)
                .filter(UserModel.id == entity_id, UserModel.user_type == "teacher")
                .first()
            )

        return user

    def delete(entity_id: str):
        """delete entity into db"""
        with session_maker() as session:
            teacher = (
                session.query(ContactModel)
                .filter(ContactModel.user_id == entity_id)
                .delete()
            )

            session.commit()

        return teacher
