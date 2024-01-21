from app.models import Task

from .base import CRUDBase


class CRUDTask(CRUDBase):
    ...


task_crud = CRUDTask(Task)
