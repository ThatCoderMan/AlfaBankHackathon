from typing import Iterable

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Sequence

from app.models import Skill

from .base import CRUDBase


class CRUDSkill(CRUDBase):
    async def get_by_query(self, session: AsyncSession, query: str):
        skills = await session.execute(
            select(Skill).where(Skill.value.ilike(f"{query}%"))
        )
        return skills.scalars().all()

    async def get_by_values_many(
        self, session: AsyncSession, skill_values: list[str]
    ) -> Sequence[Skill]:
        skills = await session.execute(
            select(Skill).where(
                func.lower(Skill.value).in_(
                    [value.lower() for value in skill_values]
                )
            )
        )
        return skills.scalars().all()

    async def get_or_create_many(
        self, session: AsyncSession, skill_values: list[str]
    ) -> Iterable[Skill]:
        skills = await self.get_by_values_many(
            session=session, skill_values=skill_values
        )
        new_skills = [
            value
            for value in skill_values
            if value.lower()
            not in [ex_value.value.lower() for ex_value in skills]
        ]
        if not new_skills:
            return skills
        session.add_all([Skill(value=value) for value in new_skills])
        await session.commit()
        skills.extend(
            await self.get_by_values_many(
                session=session, skill_valuess=new_skills
            )
        )
        return skills


skill_crud = CRUDSkill(Skill)
