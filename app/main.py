import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api import api_router
from app.auth import auth_router
from app.core.config import settings

tags_metadata = [
    {"name": "Employees", "description": "Работа с сотрудниками"},
    {"name": "PDPs", "description": "Работа с ИПР"},
    {"name": "Tasks", "description": "Работа с Задачами"},
    {
        "name": "Task Properties",
        "description": "Получение статусов и типов задач",
    },
    {"name": "Templates", "description": "Работа с шаблонами"},
]

app = FastAPI(
    title=settings.app_title,
    description=settings.description,
    openapi_tags=tags_metadata,
)

origins = [
    'http://localhost',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'http://alfabankhack.ddns.net',
    'http://alfabankhack.ddns.net:8000/',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router)
app.include_router(auth_router)

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
