from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String

Base = declarative_base()

class Product(Base):
    __tablename__ = "product"
    rollno = Column(Integer, primary_key = True)
    stname = Column(String)
    Class = Column(Integer)
    fee = Column(Float)