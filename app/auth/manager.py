import os

from fastapi import Depends
from fastapi_users import BaseUserManager, FastAPIUsers, IntegerIDMixin
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)
from fastapi_users.db import SQLAlchemyUserDatabase

from app.models.base import User
from app.auth.crud import get_user_db

SECRET = os.getenv('SECRET')


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    """
    Подключаем менеджер управления моделью,
    а так же методы управления Юзера.
    """
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET


async def get_user_manager(
        user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    """
    Функция возвращает экземпляр UserManager.
    """
    yield UserManager(user_db)


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    """
    Этот экземпляр используется для аутентификации
    пользователей с помощью токенов JWT.
    """
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)
