from pydantic import BaseModel


class StudentSchema(BaseModel):    
    name: str
    email: str
    surname: str
    city: str
    password: str
    state: bool
    contacts: list

    class Config:
        orm_mode = True
