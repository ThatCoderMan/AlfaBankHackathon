from fastapi import APIRouter

from app.schemas.user import UserRead, UserCreate
from app.core.user import auth_backend, fastapi_users

auth_router = APIRouter(prefix="/auth/jwt", tags=["auth"])

auth_router.include_router(fastapi_users.get_auth_router(auth_backend))
auth_router.include_router(fastapi_users.get_reset_password_router())
auth_router.include_router(fastapi_users.get_register_router(UserRead,
                                                             UserCreate))
