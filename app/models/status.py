from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import ENUM as PgEnum
from sqlalchemy.orm import relationship

from app.core.db import Base

from .user import UserRole

LENGTH_LIMITS_STATUS_NAME_FIELD = 50


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
