from app.models import Grade

from .base import CRUDBase


class CRUDGrade(CRUDBase):
    pass


grade_crud = CRUDGrade(Grade)
