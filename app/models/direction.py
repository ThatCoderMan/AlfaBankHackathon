from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.core.constants import LENGTH_LIMITS_VALUE_FIELDS
from app.core.db import Base


class Direction(Base):
    """Модель навыков"""

    value = Column(
        String(LENGTH_LIMITS_VALUE_FIELDS), nullable=False, unique=True
    )

    templates = relationship("Template", back_populates="direction")
