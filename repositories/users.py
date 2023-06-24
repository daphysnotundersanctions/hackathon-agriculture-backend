from sqlalchemy.orm import Session
from models.users import UsersModel, UserCreate
from typing import List



class UsersRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create_user(self, user: UserCreate):
        user = UsersModel(**user.dict())
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def get_user(self, user_id: int):
        return self.db.query(UsersModel).filter(UsersModel.id == user_id).first()
    
    def get_users(self, skip: int = 0, limit: int = 100):
        return self.db.query(UsersModel).offset(skip).limit(limit).all()
    
    def get_user_by_params(self, params: dict):
        return self.db.query(UsersModel).filter_by(**params).first()
    
   