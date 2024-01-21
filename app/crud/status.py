from app.models import Status

from .base import CRUDBase


class CRUDStatus(CRUDBase):
    ...


status_crud = CRUDStatus(Status)
