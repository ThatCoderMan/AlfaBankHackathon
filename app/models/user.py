from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class User(Base):
    """Таблица пользователей."""

    __tablename__ = "users"  # noqa

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
