from enum import Enum

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, String

from base import Base

LENGTH_LIMITS_USER_FIELDS = 150


class UserRole(Enum):
    """Выбор роли"""
    CHIEF = 'chief'
    EMPLOYEE = 'employee'


class User(SQLAlchemyBaseUserTable, Base):
    """Модель пользователя"""
    first_name = Column(
        String(LENGTH_LIMITS_USER_FIELDS),
        nullable=False
    )
    last_name = Column(
        String(LENGTH_LIMITS_USER_FIELDS),
        nullable=False
    )
    patronymic_name = Column(String(LENGTH_LIMITS_USER_FIELDS))
    position = Column(
        String(LENGTH_LIMITS_USER_FIELDS),
        nullable=False
    )
    role = Column(
        String(max(len(value.value) for value in UserRole)),
        nullable=False,
        default=UserRole.EMPLOYEE.value,
        enum=UserRole
    )
