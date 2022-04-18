from pydantic import BaseModel


class TeacherSchema(BaseModel):    
    name: str
    email: str
    surname: str
    city: str
    password: str
    state: bool
    contacts: list

    class Config:
        orm_mode = True
