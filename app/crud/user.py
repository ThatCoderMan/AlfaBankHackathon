from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User


async def get_user(db: AsyncSession, email: str):
    """Получение пользователя по email из БД."""
    result = await db.execute(select(User).filter(
        User.email == email))
    user = result.scalars().first()
    return user


async def create_user(
    db: AsyncSession,
    email: str,
    hashed_password: str,
    **kwargs
):
    """Создание нового пользователя в БД."""
    new_user = User(
        email=email,
        hashed_password=hashed_password,
        **kwargs
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
