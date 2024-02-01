from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.core.constants import LENGTH_LIMITS_SKILL_FIELDS
from app.core.db import Base


class Skill(Base):
    value = Column(
        String(LENGTH_LIMITS_SKILL_FIELDS), nullable=False, unique=True
    )

    tasks = relationship(
        'Task', secondary='task_skill', back_populates='skills'
    )
    templates = relationship(
        'Template', secondary='template_skill', back_populates='skills'
    )
