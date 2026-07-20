from fastapi import FastAPI
from module import Student

app = FastAPI()

students = [Student(rollno = 1, stname = "siva", Class = 10, fee = 20000),
           Student(rollno = 2, stname = "raja", Class = 9, fee = 18000),
           Student(rollno = 3, stname = "ramya", Class = 8, fee = 16000)]

@app.get("/students")
def students1():
    return students

@app.get("/student/{id}")
def student(id :int):
    for i in students:
        if i.rollno == id:
            return i