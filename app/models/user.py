from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    """
    Модель Юзера расширенная от стороннего пакета
    fastapi_users с добавлением новых полей
    """

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )
    first_name: Mapped[str] = mapped_column(
        String(length=20)
    )
    last_name: Mapped[str] = mapped_column(
        String(length=20)
    )
    patronymic_name: Mapped[str] = mapped_column(
        String(length=20)
    )
    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    is_active = None
    is_superuser = None
    is_verified = None
