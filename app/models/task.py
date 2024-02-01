from sqlalchemy import Column, ForeignKey, Integer, String, Table, Text
from sqlalchemy.orm import relationship

from app.core.constants import LENGTH_LIMITS_STRING_FIELDS
from app.core.db import Base

from .base import AbstractDatesModel

task_skill = Table(
    "task_skill",
    Base.metadata,
    Column("task_id", Integer, ForeignKey("task.id")),
    Column("skill_id", Integer, ForeignKey("skill.id")),
)


class Task(AbstractDatesModel):
    """Модель задач"""

    pdp_id = Column(Integer, ForeignKey("pdp.id"))
    type_id = Column(Integer, ForeignKey("type.id"))
    status_id = Column(Integer, ForeignKey("status.id"))
    title = Column(String(LENGTH_LIMITS_STRING_FIELDS), nullable=False)
    description = Column(Text, nullable=False)
    link = Column(String(LENGTH_LIMITS_STRING_FIELDS))
    chief_comment = Column(Text)
    employee_comment = Column(Text)

    skills = relationship(
        'Skill', secondary='task_skill', back_populates='tasks'
    )
    pdp = relationship("PDP", back_populates="tasks")
    type = relationship("Type", back_populates="tasks")
    status = relationship("Status", back_populates="tasks")

    @staticmethod
    def table_name():
        return 'Задача'
