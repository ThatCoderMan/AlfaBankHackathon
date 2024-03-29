from datetime import datetime
from enum import Enum as Enumer

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.dialects.postgresql import ENUM as PgEnum
from sqlalchemy.orm import relationship

from app.core.constants import (
    LENGTH_LIMITS_LINK_FIELDS,
    LENGTH_LIMITS_USER_FIELDS,
)
from app.core.db import Base


class UserRole(str, Enumer):
    """Выбор роли"""

    CHIEF = "chief"
    EMPLOYEE = "employee"


user_user = Table(
    "user_user",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id")),
    Column("chief_id", Integer, ForeignKey("user.id")),
)


class User(SQLAlchemyBaseUserTable[int], Base):
    """Модель пользователя"""

    created = Column(DateTime, default=datetime.now)
    first_name = Column(String(LENGTH_LIMITS_USER_FIELDS), nullable=False)
    last_name = Column(String(LENGTH_LIMITS_USER_FIELDS), nullable=False)
    patronymic_name = Column(String(LENGTH_LIMITS_USER_FIELDS))
    position = Column(String(LENGTH_LIMITS_USER_FIELDS), nullable=False)
    role = Column(
        PgEnum(UserRole, name='userrole', create_type=False),
        nullable=False,
        default=UserRole.EMPLOYEE,
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

    pdp = relationship("PDP", back_populates="user", uselist=False)
    templates = relationship("Template", back_populates="user")
