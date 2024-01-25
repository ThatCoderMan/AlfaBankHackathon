from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.core.db import Base

LENGTH_LIMITS_STRING_FIELDS = 100
LENGTH_LIMITS_TEXT_FIELDS = 255


class Template(Base):
    """Модель задач"""

    title = Column(String(LENGTH_LIMITS_STRING_FIELDS), nullable=False)
    description = Column(Text)
    skills = Column(String(LENGTH_LIMITS_STRING_FIELDS))
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    direction_id = Column(Integer, ForeignKey("direction.id"), nullable=False)
    grade_id = Column(Integer, ForeignKey("grade.id"), nullable=False)
    type_id = Column(Integer, ForeignKey("type.id"), nullable=False)
    duration = Column(Integer)
    recommendation = Column(Text)

    type = relationship("Type", back_populates="templates", uselist=False)
    user = relationship("User", back_populates="templates", uselist=False)
    direction = relationship(
        "Direction", back_populates="templates", uselist=False
    )
    grade = relationship("Grade", back_populates="templates", uselist=False)
