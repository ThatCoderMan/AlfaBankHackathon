from typing import Iterable

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Sequence

from app.models import Skill

from .base import CRUDBase


class CRUDSkill(CRUDBase):
    async def get_by_names_many(
        self, session: AsyncSession, skill_names: list[str]
    ) -> Sequence[Skill]:
        skills = await session.execute(
            select(Skill).where(
                func.lower(Skill.name).in_(
                    [name.lower() for name in skill_names]
                )
            )
        )
        return skills.scalars().all()

    async def get_or_create_many(
        self, session: AsyncSession, skill_names: list[str]
    ) -> Iterable[Skill]:
        skills = await self.get_by_names_many(
            session=session, skill_names=skill_names
        )
        new_skills = [
            name
            for name in skill_names
            if name.lower() not in [ex_name.name.lower() for ex_name in skills]
        ]
        if not new_skills:
            return skills
        session.add_all([Skill(name=name) for name in new_skills])
        await session.commit()
        skills.extend(
            await self.get_by_names_many(
                session=session, skill_names=new_skills
            )
        )
        return skills


skill_crud = CRUDSkill(Skill)
