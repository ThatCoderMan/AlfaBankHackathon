from datetime import datetime
from enum import Enum as Enumer

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    Table,
)
from sqlalchemy.orm import relationship

from app.core.db import Base

LENGTH_LIMITS_USER_FIELDS = 150
LENGTH_LIMITS_LINK_FIELDS = 200


class UserRole(Enumer):
    """Выбор роли"""

    CHIEF = "chief"
    EMPLOYEE = "employee"


user_user = Table(
    "user_user",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id")),
    Column("chief_id", Integer, ForeignKey("user.id")),
)


class User(SQLAlchemyBaseUserTable, Base):
    """Модель пользователя"""

    created = Column(DateTime, default=datetime.now)
    first_name = Column(String(LENGTH_LIMITS_USER_FIELDS), nullable=False)
    last_name = Column(String(LENGTH_LIMITS_USER_FIELDS), nullable=False)
    patronymic_name = Column(String(LENGTH_LIMITS_USER_FIELDS))
    position = Column(String(LENGTH_LIMITS_USER_FIELDS), nullable=False)
    role = Column(
        Enum(UserRole).with_variant(
            String(max(len(value.value) for value in UserRole)),
            "sqlite",
            "postgresql",
        ),
        nullable=False,
        default=UserRole.EMPLOYEE.value,
    )
    chief = relationship(
        "User",
        secondary=user_user,
        back_populates="chief",
        foreign_keys=[user_user.c.chief_id],
    )
    employee = relationship(
        "User",
        secondary=user_user,
        back_populates="employee",
        foreign_keys=[user_user.c.user_id],
    )
    photo = Column(String(LENGTH_LIMITS_LINK_FIELDS))
