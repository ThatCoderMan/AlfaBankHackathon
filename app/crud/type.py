from app.models import Type
from .base import CRUDBase


class CRUDType(CRUDBase):
    pass


type_crud = CRUDType(Type)
