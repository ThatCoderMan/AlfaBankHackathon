from enum import Enum

from sqlalchemy import Column, ForeignKey, Integer, String, Table, Text
from sqlalchemy.orm import relationship

from base import AbstractDatesModel, Base


LENGTH_LIMITS_STRING_FIELDS = 100
LENGTH_LIMITS_TEXT_FIELDS = 255
LENGTH_LIMITS_SKILL_NAME_FIELD = 50


class Status(Enum):
    """Выбор статуса"""
    REQUEST = 'Заявка'
    IN_WORK = 'В работе'
    DONE = 'Выполнена'
    CANCEL = 'Отменена'
    EXECUTE = 'Исполнена'


pdp_skill = Table(
    'pdp_skill',
    Base.metadata,
    Column('pdp_id', Integer, ForeignKey('pdp.id')),
    Column('skill_id', Integer, ForeignKey('skill.id'))
)

task_skill = Table(
    'pdp_skill',
    Base.metadata,
    Column('task_id', Integer, ForeignKey('task.id')),
    Column('skill_id', Integer, ForeignKey('skill.id'))
)


class Skill(Base):
    """Модель навыков"""
    name = Column(
        String(LENGTH_LIMITS_SKILL_NAME_FIELD),
        nullable=False,
        unique=True
    )
    pdp = relationship(
        "PDP",
        secondary=pdp_skill,
        back_populates="skill"
    )
    task = relationship(
        "Task",
        secondary=task_skill,
        back_populates="skill"
    )


class PDP(Base, AbstractDatesModel):
    """Модель ИПР"""
    user_id = Column(
        Integer,
        ForeignKey('user.id')
    )
    status = Column(
        String(max(len(value.value) for value in Status)),
        default=Status.IN_WORK.value,
        enum=Status
    )

    skills = relationship("Skill", secondary=pdp_skill, back_populates="pdp")


class Task(Base, AbstractDatesModel):
    """Модель задач"""
    pdp_id = Column(Integer, ForeignKey('pdp.id'))
    type = Column(String(LENGTH_LIMITS_STRING_FIELDS), nullable=False)
    description = Column(Text(LENGTH_LIMITS_TEXT_FIELDS), nullable=False)
    chief_comment_id = Column(Integer, ForeignKey('comment.id'))
    employee_comment_id = Column(Integer, ForeignKey('comment.id'))
    skills = relationship("Skill", secondary=task_skill, back_populates="task")


class Comment(Base):
    """Модель комментариев"""
    task_id = Column(Integer, ForeignKey('task.id'))
    comment = Column(Text(LENGTH_LIMITS_TEXT_FIELDS), nullable=False)
