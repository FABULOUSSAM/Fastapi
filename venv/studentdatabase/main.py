from fastapi import FastAPI,Depends,status,Response
from pydantic import BaseModel
from sqlalchemy.sql.functions import mode
from studentdatabase import models
from studentdatabase.database import engine,SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()



models.Base.metadata.create_all(engine)

class Student(BaseModel):
    name:str
    marks:int


@app.post("/insertdata",status_code=status.HTTP_201_CREATED)
def insert(student:Student,db:Session=Depends(get_db)):
    #return {"Name":student.name,"Marks":student.marks}
    new_marks=models.Student(name=student.name,marks=student.marks)
    db.add(new_marks)
    db.commit()
    db.refresh(new_marks)
    return new_marks

@app.get("/receivedata")
def getdata(db:Session=Depends(get_db)):
    marks=db.query(models.Student).all()
    return marks

@app.get("/receivedata/{id}", status_code=200)
def getdataid(*,id:int,db:Session=Depends(get_db),response: Response):
    marks=db.query(models.Student).filter(models.Student.id==id).first()
    if not marks:
        response.status_code=status.HTTP_404_NOT_FOUND
    return marks

@app.put("/updatedata/{id}",status_code=status.HTTP_200_OK)
def updatedata(*,id:int,db:Session=Depends(get_db),student:Student):
    db.query(models.Student).filter(models.Student.id==id).update(student)
    db.commit()
    return "Updated Succefully"



@app.delete("/deleteitem/{id}",status_code=status.HTTP_204_NO_CONTENT)
def deleteid(*,id:int,db:Session=Depends(get_db),response: Response):
    db.query(models.Student).filter(models.Student.id==id).delete(synchronize_session=False)
    db.commit()
    return {"Id has been deleted"}


