from fastapi import FastAPI

from app.api.routers import api_router
from app.auth.routers import api_version1
from app.core.config import settings

app = FastAPI(title=settings.app_title, description=settings.description)

app.include_router(api_router)
app.include_router(api_version1)
