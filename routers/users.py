from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from repositories.users import UsersRepository
from database.get_db import get_db
from models.users import UserCreate

from typing import List

router = APIRouter()


@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.
    """
    user_repo = UsersRepository(db)
    return user_repo.create_user(user)

@router.get("/")
def get_all_users(db: Session = Depends(get_db)):
    """
    Get all users.
    """
    user_repo = UsersRepository(db)
    users = user_repo.get_users()
    return users

@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Get a specific user by ID.
    """
    user_repo = UsersRepository(db)
    user = user_repo.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/params")
def get_user_by_params(params: dict, db: Session = Depends(get_db)):
    """
    Get a user based on specified parameters.
    """
    user_repo = UsersRepository(db)
    user = user_repo.get_user_by_params(params)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
