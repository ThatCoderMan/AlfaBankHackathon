from sqlalchemy import Column, Enum, String

from app.core.db import Base

from .user import UserRole

LENGTH_LIMITS_TYPE_NAME_FIELD = 50


class Status(Base):
    """Модель навыков"""

    name = Column(
        String(LENGTH_LIMITS_TYPE_NAME_FIELD), nullable=False, unique=True
    )
    role = Column(
        Enum(UserRole).with_variant(
            String(max(len(value.value) for value in UserRole)),
            "sqlite",
            "postgresql",
        ),
        nullable=False,
    )
