from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
Base = declarative_base()


class UsersModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    login = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False)




class UserCreate(BaseModel):
    login: str
    password: str
    status: str
