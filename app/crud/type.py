from app.models import Type

from .base import CRUDBase


class CRUDType(CRUDBase):
    pass


grade_crud = CRUDType(Type)
