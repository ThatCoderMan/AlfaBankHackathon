from fastapi import APIRouter

from app.auth.schemas import UserRead, UserCreate
from app.auth.manager import auth_backend, fastapi_users

api_version1 = APIRouter(prefix="/auth/jwt", tags=["auth"])


api_version1.include_router(fastapi_users.get_auth_router(auth_backend))
api_version1.include_router(fastapi_users.get_reset_password_router())
api_version1.include_router(fastapi_users.get_register_router(UserRead,
                                                              UserCreate))
