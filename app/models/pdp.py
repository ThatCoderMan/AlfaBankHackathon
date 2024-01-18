from enum import Enum as Enumer

from sqlalchemy import Column, Enum, ForeignKey, Integer, String, Table, Text
from sqlalchemy.orm import relationship

from base import AbstractDatesModel, Base
from users import User


LENGTH_LIMITS_STRING_FIELDS = 100
LENGTH_LIMITS_TEXT_FIELDS = 255
LENGTH_LIMITS_SKILL_NAME_FIELD = 50


class Status(Enumer):
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
    'task_skill',
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


class PDP(AbstractDatesModel):
    """Модель ИПР"""
    user_id = Column(
        Integer,
        ForeignKey('user.id')
    )
    status = Column(
        Enum(Status).with_variant(
            String(max(len(value.value) for value in Status)),
            'sqlite',
            'postgresql'),
        default=Status.IN_WORK.value,
    )

    skills = relationship("Skill", secondary=pdp_skill, back_populates="pdp")


class Task(AbstractDatesModel):
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
