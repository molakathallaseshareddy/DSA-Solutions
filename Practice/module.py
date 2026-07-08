from pydantic import BaseModel

class Student(BaseModel):
    sno : int
    name : str
    clas : int
    rno : int
    fee : float
