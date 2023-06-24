from sqlalchemy.orm import Session
from models.tasks import TasksModel, TaskCreate
from fastapi import HTTPException

class TasksRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create_task(self, data: TaskCreate):
        try:
            task = TasksModel(**data.dict())
            self.db.add(task)
            self.db.commit()
            self.db.refresh(task)
            return data
        except Exception as e:
            print(e)
            if(str(e).find("Duplicate entry") != -1):
                raise HTTPException(status_code=400, detail="Task already exists")
            elif(str(e).find("foreign key") != -1):
                raise HTTPException(status_code=400, detail="User not found")
            return None
    
    def get_task(self, task_id: int):
        return self.db.query(TasksModel).filter(TasksModel.id == task_id).first()
    
    def get_user_tasks(self, user_id: int):
        return self.db.query(TasksModel).filter(TasksModel.user_id == user_id).all()
    
    
    def get_tasks(self, skip: int = 0, limit: int = 100):
        return self.db.query(TasksModel).offset(skip).limit(limit).all()
    
    def get_task_by_params(self, params: dict):
        return self.db.query(TasksModel).filter_by(**params).first()
