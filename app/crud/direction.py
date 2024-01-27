from app.models import Direction

from .base import CRUDBase


class CRUDDirection(CRUDBase):
    pass


direction_crud = CRUDDirection(Direction)
