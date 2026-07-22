from fastapi import FastAPI
from module import Student
import database_models
from database import session, engine

database_models.Base.metadata.create_all(bind = engine)

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

@app.post("/add_student")
def add_student(student : Student):
    students.append(student)
    return student

@app.put("/update_student/{id}")
def update_student(id : int, student: Student):
    for i in range(len(students)):
        if students[i].rollno == id:
            students[i] = student
            return {"message" : "Student is updated"}

@app.delete("/delete_student/{id}")
def delete_student(id : int):
    for i in students:
        if i.rollno == id:
            students.remove(i)
            return {"student is deleted"}