from sqlalchemy import Column, ForeignKey, Integer, String, Text

from base import AbstractDatesModel


LENGTH_LIMITS_STRING_FIELDS = 100
LENGTH_LIMITS_TEXT_FIELDS = 255


class Task(AbstractDatesModel):
    """Модель задач"""
    pdp_id = Column(Integer, ForeignKey('pdp.id'))
    type = Column(Integer, ForeignKey('type.id'))
    description = Column(Text(LENGTH_LIMITS_TEXT_FIELDS), nullable=False)
    skills = Column(String(LENGTH_LIMITS_STRING_FIELDS), nullable=False)
    chief_comment = Column(Text(LENGTH_LIMITS_TEXT_FIELDS))
    employee_comment = Column(Text(LENGTH_LIMITS_TEXT_FIELDS))
    status = Column(Integer, ForeignKey('status.id'))
