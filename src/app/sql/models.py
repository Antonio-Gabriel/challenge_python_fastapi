from datetime import datetime
from sqlalchemy import Column, Boolean, String, TIMESTAMP, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import declarative_base

from .enums.Users import Users

Base = declarative_base()


class UserModel(Base):
    __tablename__ = "tusers"

    id = Column(String(40), primary_key=True)
    password = Column(String(120), nullable=False)
    name = Column(String(60), nullable=False)
    surname = Column(String(60), nullable=False)
    email = Column(String(60), nullable=False)
    state = Column(Boolean, default=True)
    city = Column(String(45), nullable=False)
    user_type = Column(ENUM(Users), nullable=False)

    def __repr__(self) -> str:
        return f"UserModel(id={self.id}, name={self.name}, surname={self.surname}, email={self.email}, password={self.password}, city={self.city}, state={self.state}, user_type={self.user_type})"


class TeacherModel(Base):
    __tablename__ = "teachers"

    id = Column(String(40), nullable=False, primary_key=True)
    user_id = Column(String(40), ForeignKey("tusers.id"))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)


class StudentModel(Base):
    __tablename__ = "students"

    id = Column(String(40), nullable=False, primary_key=True)
    user_id = Column(String(40), ForeignKey("tusers.id"))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)


class CourseModel(Base):
    __tablename__ = "courses"

    id = Column(String(40), nullable=False, primary_key=True)
    name = Column(String(60), nullable=False)
    startDate = Column(DateTime, nullable=False)
    endDate = Column(DateTime, nullable=False)
    state = Column(Boolean, default=True)
    teacher_id = Column(String(40), ForeignKey("teachers.id"))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)


class EnrollmentModel(Base):
    __tablename__ = "enrollments"

    student_id = Column(String(40), ForeignKey("students.id"), primary_key=True)
    course_id = Column(String(40), ForeignKey("courses.id"), primary_key=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)


class ContactModel(Base):
    __tablename__ = "contacts"

    id = Column(String(40), nullable=False, primary_key=True)
    phone = Column(String(40), nullable=False, primary_key=True)
    user_id = Column(String(40), ForeignKey("tusers.id"))
