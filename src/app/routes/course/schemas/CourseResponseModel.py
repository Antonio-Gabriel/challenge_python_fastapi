from datetime import datetime
from typing import List
from pydantic import BaseModel


class TeacherModel(BaseModel):
    id: int
    name: str
    email: str


class CourseModel(BaseModel):
    id: int
    name: str
    startDate: datetime
    endDate: datetime
    state: bool
    teacher: TeacherModel


class CourseResponseModel(BaseModel):
    courses: List[CourseModel]
