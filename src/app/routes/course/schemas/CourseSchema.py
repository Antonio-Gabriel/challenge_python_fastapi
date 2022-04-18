from datetime import datetime
from pydantic import BaseModel


class CourseSchema(BaseModel):
    name: str
    startDate: datetime
    endDate: datetime
    state: bool
    teacher_id: int

    class Config:
        orm_mode = True
