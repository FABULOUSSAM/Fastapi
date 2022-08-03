from .database import Base
from sqlalchemy import Column, Integer, String
class Student(Base):
    __tablename__="marks"
    id = Column(Integer, primary_key=True,index=True)
    name=Column(String)
    marks=Column(Integer)