from database import Base
from sqlalchemy import Column, Integer, String, Float


class Student(Base):
    __tablename__ = "students"
    
    sid = Column(Integer, primary_key = True, index = True)
    sname = Column(String(20))
    fee = Column(Float)