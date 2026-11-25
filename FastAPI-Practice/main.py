from fastapi import FastAPI, Depends
from sqlalchemy.orm import session
from models import Student
from database import get_db, Base, engine


Base.metadata.create_all(bind = engine)
app = FastAPI()

@app.get("/")
def display():
    return "Welcome to FastAPI learning"