from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .base import AbstractDatesModel

LENGTH_LIMITS_STRING_FIELDS = 100
LENGTH_LIMITS_TEXT_FIELDS = 255


class Task(AbstractDatesModel):
    """Модель задач"""

    pdp_id = Column(Integer, ForeignKey("pdp.id"))
    type_id = Column(Integer, ForeignKey("type.id"))
    status_id = Column(Integer, ForeignKey("status.id"))
    title = Column(String(LENGTH_LIMITS_STRING_FIELDS), nullable=False)
    description = Column(Text, nullable=False)
    skills = Column(String(LENGTH_LIMITS_STRING_FIELDS), nullable=False)
    chief_comment = Column(Text)
    employee_comment = Column(Text)

    pdp = relationship("PDP", back_populates="tasks")
    type = relationship("Type", back_populates="tasks")
    status = relationship("Status", back_populates="tasks")
