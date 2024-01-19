from app.core.db import Base


class BaseAbstractModel(Base):
    __abstract__ = True
