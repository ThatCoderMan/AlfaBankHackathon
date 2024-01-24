from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Status
from .base import CRUDBase


class CRUDStatus(CRUDBase):
    async def get_multi_by_role(self, session: AsyncSession, user: object):
        db_objs = await session.execute(
            select(self.model).where(self.model.role == user.role)
        )
        return db_objs.scalars().all()


status_crud = CRUDStatus(Status)
