from module import Student
from fastapi import FastAPI

students = [Student(sno = 1, name = "seshareddy", clas =  1, rno = 48, fee = 5000),
            Student(sno = 2, name = "samba", clas =  1, rno = 46, fee = 5000),
            Student(sno = 1, name = "meka", clas =  2, rno = 23, fee = 7000),]

app = FastAPI()
@app.get("/students")
def students_data():
    return students

@app.get("/students/{no}")
def student_get(no : int):
    for i in students:
        if i.sno == no:
            return i
    return {"Message" : "Student ID = {no} is not Available"}

@app.post("/addstudent")
def add_student(student :Student):
    students.append(student)
    return {"Message" : "Student added successfully"}