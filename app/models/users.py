from enum import Enum as Enumer

from fastapi_users import SQLAlchemyBaseUserTable
from sqlalchemy import Column, Enum, ForeignKey, Integer, String

from base import Base

LENGTH_LIMITS_USER_FIELDS = 150
LENGTH_LIMITS_LINK_FIELDS = 200


class UserRole(Enumer):
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
        Enum(UserRole).with_variant(
            String(max(len(value.value) for value in UserRole)),
            'sqlite',
            'postgresql'),
        nullable=False,
        default=UserRole.EMPLOYEE.value
    )
    chief_id = Column(Integer, ForeignKey('user.id'))
    photo = Column(String(LENGTH_LIMITS_LINK_FIELDS))
