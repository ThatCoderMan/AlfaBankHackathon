from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.models import Task

from .base import CRUDBase


class CRUDTask(CRUDBase):
    async def get(
        self,
        task_id: int,
        session: AsyncSession,
    ):
        result = await session.execute(
            select(Task)
            .options(joinedload(Task.type), joinedload(Task.status))
            .where(Task.id == task_id)
        )
        return result.scalars().first()


task_crud = CRUDTask(Task)
