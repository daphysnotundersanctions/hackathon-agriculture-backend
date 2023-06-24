from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.users import UsersModel
from pydantic import BaseModel

Base = declarative_base()


class TasksModel(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey(UsersModel.id))

    user = relationship(UsersModel, backref="tasks")
    # Define any other columns for the TasksModel here


class TaskCreate(BaseModel):
    title: str
    description: str
    user_id: int
