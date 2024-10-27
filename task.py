from email.policy import default
from user import *
from fastapi import APIRouter
from app.backend.db import Base
from sqlalchemy import Column,Integer, String, ForeignKey,Boolean
from sqlalchemy.orm import relationship, defer

router = APIRouter(prefix = '/task', tags = ["task"])

class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key= True, index= True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default = 0)
    completed = Column(Boolean, default = False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index = True)
    slug = Column(String, unique= True, index = True )


    user = relationship('User', back_populates= "tasks")

from sqlalchemy.schema import CreateTable
print(CreateTable(Task.__table__))

@router.get("/")
async def get_all_tasks():
    pass

@router.get("/task_id")
async def task_by_id():
    pass

@router.post("/create")
async def create_task():
    pass

@router.put("/update")
async def update_task():
    pass

@router.delete("/delete")
async def delete_task():
    pass