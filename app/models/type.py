from sqlalchemy import Column, String

from app.core.db import Base

LENGTH_LIMITS_TYPE_NAME_FIELD = 50


class Type(Base):
    """Модель навыков"""

    name = Column(
        String(LENGTH_LIMITS_TYPE_NAME_FIELD), nullable=False, unique=True
    )
