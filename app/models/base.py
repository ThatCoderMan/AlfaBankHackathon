from datetime import datetime

from sqlalchemy import Column, Date

from core.db import Base


class AbstractDatesModel(Base):
    """Абстрактная модель с датами начала и окончания"""
    __abstract__ = True
    starting_date = Column(Date(), default=datetime.date.now)
    deadline = Column(Date(), nullable=False)
