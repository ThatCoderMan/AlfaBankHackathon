from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.models import Skill, Template

from . import skill_crud
from .base import CRUDBase


class CRUDTemplate(CRUDBase):
    async def get_multi(
        self,
        session: AsyncSession,
        q: str = None,
        direction: int = None,
        skills: list[int] = None,
        grade: list[str] = None,
        type: str = None,
        duration_from: int = None,
        duration_to: int = None,
        creator: int = None,
    ):
        filters = []
        if q is not None:
            filters.append(Template.title.ilike(f'%{q}%'))
        if direction is not None:
            filters.append(Template.direction_id == direction)
        if skills is not None:
            filters.append(Template.skills.any(Skill.id.in_(skills)))
        if grade is not None:
            filters.append(Template.grade_id.in_(grade))
        if type is not None:
            filters.append(Template.type_id == type)
        if duration_from is not None:
            filters.append(Template.duration >= duration_from)
        if duration_to is not None:
            filters.append(Template.duration <= duration_to)
        if creator is not None:
            filters.append(Template.user_id == creator)

        query = select(Template).where(and_(*filters))

        result = await session.execute(
            query.options(
                joinedload(Template.type),
                joinedload(Template.direction),
                joinedload(Template.grade),
                joinedload(Template.user),
                joinedload(Template.skills),
            )
        )
        return result.unique().scalars().all()

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


template_crud = CRUDTemplate(Template)
