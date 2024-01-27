from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import ENUM as PgEnum
from sqlalchemy.orm import relationship

from app.core.constants import LENGTH_LIMITS_VALUE_FIELDS
from app.core.db import Base

from .user import UserRole


class Status(Base):
    """Модель навыков"""

    value = Column(
        String(LENGTH_LIMITS_VALUE_FIELDS), nullable=False, unique=True
    )
    role = Column(
        PgEnum(UserRole, name='userrole', create_type=False),
        nullable=False,
    )

    tasks = relationship("Task", back_populates="status")
