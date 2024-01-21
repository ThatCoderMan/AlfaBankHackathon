from app.models import User

from .base import CRUDBase


class CRUDUser(CRUDBase):
    ...


user_crud = CRUDUser(User)
