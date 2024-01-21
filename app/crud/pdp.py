from app.models import PDP

from .base import CRUDBase


class CRUDpdp(CRUDBase):
    ...


pdp_crud = CRUDpdp(PDP)
