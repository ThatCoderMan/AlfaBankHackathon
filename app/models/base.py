from app.core.db import Base

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column


class BaseAbstractModel(Base):
    __abstract__ = True


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
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
    )
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
