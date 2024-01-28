from fastapi import HTTPException, status
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.models import Task

from .base import CRUDBase
from .skill import skill_crud


class CRUDTask(CRUDBase):
    async def get(
        self,
        task_id: int,
        session: AsyncSession,
    ):
        db_obj = await session.execute(
        db_obj = await session.execute(
            select(Task)
            .options(
                joinedload(Task.type),
                joinedload(Task.status),
                joinedload(Task.skills),
            )
            .where(Task.id == task_id)
        )
        result = db_obj.scalars().first()

        if result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'Task {task_id} not found')

        return result

    async def update(
        self,
        db_obj,
        obj_in,
        session: AsyncSession,
    ):
        obj_in.skills = await skill_crud.get_or_create_many(
            session=session, skill_values=obj_in.skills
        )
        await session.refresh(db_obj)
        db_task = await super().update(
            obj_in=obj_in, db_obj=db_obj, session=session
        )
        return db_task

    async def create(self, obj_in, session: AsyncSession, **extra_fields):
        obj_in.skills = await skill_crud.get_or_create_many(
            session=session, skill_values=obj_in.skills
        )
        db_task = await super().create(
            obj_in=obj_in, session=session, **extra_fields
        )
        return db_task


task_crud = CRUDTask(Task)
