from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.core.constants import LENGTH_LIMITS_VALUE_FIELDS
from app.core.db import Base


class Type(Base):
    """Модель навыков"""

    value = Column(
        String(LENGTH_LIMITS_VALUE_FIELDS), nullable=False, unique=True
    )

    tasks = relationship("Task", back_populates="type")
    templates = relationship("Template", back_populates="type")
