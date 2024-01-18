from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.base import User
from app.core.db import get_async_session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    """
    Возвращает экземпляр базы данных пользователей,
    связанный с предоставленным экземпляром AsyncSession.
    """
    yield SQLAlchemyUserDatabase(session, User)
