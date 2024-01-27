from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import ENUM as PgEnum
from sqlalchemy.orm import relationship

from app.core.db import Base
from core.constants import LENGTH_LIMITS_STATUS_NAME_FIELD
from .user import UserRole


class Status(Base):
    """Модель навыков"""

    name = Column(
        String(LENGTH_LIMITS_STATUS_NAME_FIELD), nullable=False, unique=True
    )
    role = Column(
        PgEnum(UserRole, name='userrole', create_type=False),
        nullable=False,
    )

    tasks = relationship("Task", back_populates="status")
