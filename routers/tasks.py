from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from repositories.tasks import TasksRepository
from database.get_db import get_db
from models.tasks import TasksModel, TaskCreate

from typing import List

router = APIRouter()


@router.post("/")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    """
    Create a new task.
    """
    task_repo = TasksRepository(db)
    return task_repo.create_task(task)

@router.get("/")
def get_all_tasks(db: Session = Depends(get_db)):
    """
    Get all tasks.
    """
    task_repo = TasksRepository(db)
    tasks = task_repo.get_tasks()
    return tasks

@router.get("/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    """
    Get a specific task by ID.
    """
    task_repo = TasksRepository(db)
    task = task_repo.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.get("/user/{user_id}")
def get_user_tasks(user_id: int, db: Session = Depends(get_db)):
    """
    Get tasks assigned to a specific user.
    """
    task_repo = TasksRepository(db)
    tasks = task_repo.get_user_tasks(user_id)
    if tasks is None:
        raise HTTPException(status_code=404, detail="Tasks not found")
    return tasks

@router.post("/params")
def get_task_by_params(params: dict, db: Session = Depends(get_db)):
    """
    Get a task based on specified parameters.
    """
    task_repo = TasksRepository(db)
    task = task_repo.get_task_by_params(params)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
