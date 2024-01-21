import uvicorn
from fastapi import FastAPI

from app.api.routers import api_router
from app.auth import auth_router
from app.core.config import settings

app = FastAPI(title=settings.app_title, description=settings.description)

app.include_router(api_router)
app.include_router(auth_router)


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
