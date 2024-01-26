from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.core.db import Base

LENGTH_LIMITS_SKILL_NAME_FIELD = 30


class Skill(Base):
    value = Column(
        String(LENGTH_LIMITS_SKILL_NAME_FIELD), nullable=False, unique=True
    )

    tasks = relationship(
        'Task', secondary='task_skill', back_populates='skills'
    )
    templates = relationship(
        'Template', secondary='template_skill', back_populates='skills'
    )
