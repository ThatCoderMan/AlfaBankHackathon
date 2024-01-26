from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.core.constants import LENGTH_LIMITS_TYPE_NAME_FIELD
from app.core.db import Base


class Type(Base):
    """Модель навыков"""

    name = Column(
        String(LENGTH_LIMITS_TYPE_NAME_FIELD), nullable=False, unique=True
    )

    tasks = relationship("Task", back_populates="type")
