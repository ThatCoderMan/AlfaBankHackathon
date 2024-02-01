from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.constants import LENGTH_LIMITS_STRING_FIELDS

from .base import AbstractDatesModel


class PDP(AbstractDatesModel):
    """Модель ИПР"""

    user_id = Column(Integer, ForeignKey("user.id"))
    goal = Column(String(LENGTH_LIMITS_STRING_FIELDS), nullable=False)

    tasks = relationship("Task", back_populates="pdp")
    user = relationship("User", back_populates="pdp", uselist=False)

    @classmethod
    def __str__(cls):
        return 'ИПР'
