from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String

Base = declarative_base()

class Student(Base):
    __tablename__ = "student"
    rollno = Column(Integer, primary_key = True)
    stname = Column(String(50))
    Class = Column(Integer)
    fee = Column(Float)