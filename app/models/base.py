from datetime import datetime

from sqlalchemy import Column, Date, Integer
from sqlalchemy.orm import declarative_base, declared_attr


class BaseModel:
    """Основа для таблиц БД"""

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=BaseModel)


class AbstractDatesModel(Base):
    """Абстрактная модель с датами начала и окончания"""
    __abstract__ = True
    starting_date = Column(Date(), default=datetime.date.now)
    deadline = Column(Date(), nullable=False)
