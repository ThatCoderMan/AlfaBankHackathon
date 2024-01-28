from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.models import Template

from . import skill_crud
from .base import CRUDBase


class CRUDTemplate(CRUDBase):
    async def get(
        self,
        template_id: int,
        session: AsyncSession,
    ):
        result = await session.execute(
            select(Template)
            .options(
                joinedload(Template.type),
                joinedload(Template.direction),
                joinedload(Template.grade),
                joinedload(Template.user),
                joinedload(Template.skills),
            )
            .where(Template.id == template_id)
        )
        return result.scalars().first()

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
        db_template = await super().update(
            obj_in=obj_in, db_obj=db_obj, session=session
        )
        return db_template

    async def create(self, obj_in, session: AsyncSession, **extra_fields):
        obj_in.skills = await skill_crud.get_or_create_many(
            session=session, skill_values=obj_in.skills
        )
        db_template = await super().create(
            obj_in=obj_in, session=session, **extra_fields
        )
        return db_template

    async def create_from_dict(self, data: dict, session: AsyncSession):
        db_obj = self.model(**data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj


template_crud = CRUDTemplate(Template)
