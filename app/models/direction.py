from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.core.db import Base

LENGTH_LIMITS_TYPE_NAME_FIELD = 50


class Direction(Base):
    """Модель навыков"""

    name = Column(
        String(LENGTH_LIMITS_TYPE_NAME_FIELD), nullable=False, unique=True
    )

    templates = relationship("Template", back_populates="direction")
