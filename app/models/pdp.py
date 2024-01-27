from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import AbstractDatesModel
from core.constants import LENGTH_LIMITS_STRING_FIELDS


class PDP(AbstractDatesModel):
    """Модель ИПР"""

    user_id = Column(Integer, ForeignKey("user.id"))
    goal = Column(String(LENGTH_LIMITS_STRING_FIELDS), nullable=False)

    tasks = relationship("Task", back_populates="pdp")
    user = relationship("User", back_populates="pdp", uselist=False)
