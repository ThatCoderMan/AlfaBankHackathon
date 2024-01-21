from app.models import Type

from .base import CRUDBase


class CRUDType(CRUDBase):
    ...


type_crud = CRUDType(Type)
