from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, NumberNotMultipleError
app = FastAPI()

student={
    1:{
        "name":"Shubam",
        "rollno":"18CE7007",
        "year":5
    },
    2:{
        "name":"SAM",
        "rollno":"18DE7007",
        "year":6
    }
}

# class Students(BaseModel):
#     name:str
#     rollno:str
#     year:int
class Studentdata(BaseModel):
    name:str
    rollno:str
    year:int

class UpdateStudentdata(BaseModel):
    name:Optional[str]=None
    rollno:Optional[str]=None
    year:Optional[int]=None


@app.delete("/deletevalue/{studentid}")
async def delete(studentid:int):
    if studentid not in student:
        return {"Error":"Value not present in the database"}
    else:
        del student[studentid]
@app.put("/updatevalue/{studentid}")
async def update(studentid:int,studentdata:UpdateStudentdata):
    if studentid not in student:
        return {"Error":"UPDATION DATA IS NOT PRESENT"}
    else:
        if studentdata.name!=None:
            student[studentid].name=studentdata.name

        if studentdata.rollno!=None:
            student[studentid].rollno=studentdata.rollno

        if studentdata.year!=None:
            student[studentid].year=studentdata.year

        #student[studentid]=studentdata
        return student[studentid]

@app.post("/createstudent/{studentid}")
async def create(studentid:int,studentdata:Studentdata):
    if studentid in student:
        return {"Error":"Value already present"}
    else:
        student[studentid]=studentdata
        return student[studentid]
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/student/{student_id}")
def printval(student_id :int):
    return student[student_id]

# @app.post("/createstudent/{student__id}")
# def createstudent(stundent_id:int,students=Students):
#     if stundent_id in student:
#         return {"Error":"Data Already exits in database"}
#     student[stundent_id]=students
#     return student[stundent_id]
