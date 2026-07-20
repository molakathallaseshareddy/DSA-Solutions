from pydantic import BaseModel

class Student(BaseModel):
    rollno : int
    stname : str
    Class : int
    fee : float