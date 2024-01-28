from sqlalchemy import Column, Date

from app.core.db import Base


class AbstractDatesModel(Base):
    """Абстрактная модель с датами начала и окончания"""

    __abstract__ = True
    starting_date = Column(Date())
    deadline = Column(Date())
