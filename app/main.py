from fastapi import FastAPI

from app.api.routers import main_router
from app.auth.routers import auth_router
from app.core.config import settings

app = FastAPI(title=settings.app_title, description=settings.description)

app.openapi = {
    "info": {
        "title": "API для управления ИПР и сотрудниками",
        "version": "1.0",
        "description": "API предоставляет возможности по управлению "
        "индивидуальными планами развития (ИПР) и данными о "
        "сотрудниках организации.",
    },
    "security": [{"oauth2": ["read", "write"]}],
    "servers": None,
}


app.include_router(main_router)
app.include_router(auth_router)
