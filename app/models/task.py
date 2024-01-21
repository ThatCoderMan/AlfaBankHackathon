from sqlalchemy import Column, ForeignKey, Integer, String, Text

from .base import AbstractDatesModel

LENGTH_LIMITS_STRING_FIELDS = 100
LENGTH_LIMITS_TEXT_FIELDS = 255


class Task(AbstractDatesModel):
    """Модель задач"""

    pdp_id = Column(Integer, ForeignKey("pdp.id"))
    type = Column(Integer, ForeignKey("type.id"))
    description = Column(Text, nullable=False)
    skills = Column(String(LENGTH_LIMITS_STRING_FIELDS), nullable=False)
    chief_comment = Column(Text)
    employee_comment = Column(Text)
    status = Column(Integer, ForeignKey("status.id"))