from fastapi import HTTPException, status
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
        db_obj = await session.execute(
            select(Task)
            .options(joinedload(Task.type), joinedload(Task.status))
            .where(Task.id == task_id)
        )
        result = db_obj.scalars().first()

        if result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return result


task_crud = CRUDTask(Task)
