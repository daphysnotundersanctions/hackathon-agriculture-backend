from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import users, tasks
from database import get_db

# Создание экземпляра приложения FastAPI
app = FastAPI()
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])

# Добавление CORS-мидлвары
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешаем все источники
    allow_methods=["*"],  # Разрешаем все HTTP-методы
    allow_headers=["*"],  # Разрешаем все заголовки
)

