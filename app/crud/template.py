from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.models import Template

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
            )
            .where(Template.id == template_id)
        )
        return result.scalars().first()

    pass


template_crud = CRUDTemplate(Template)
