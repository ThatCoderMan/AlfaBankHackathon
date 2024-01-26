from fastapi import HTTPException, status
from sqlalchemy import Result, Select, alias, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import aliased, joinedload
from sqlalchemy.sql.elements import BinaryExpression

from app.models import PDP, Status, Task

from .base import CRUDBase
from .mixin import StatisticMixin

status_alias = aliased(Status)
task_alias = aliased(Task)


class CRUDpdp(CRUDBase, StatisticMixin):
    @staticmethod
    async def __get_execute(
        session: AsyncSession,
        where_option: BinaryExpression,
        done_subquery: Select,
        total_subquery: Select,
    ) -> Result:
        return await session.execute(
            select(PDP, done_subquery, total_subquery)
            .options(joinedload(PDP.tasks))
            .options(
                joinedload(PDP.tasks).joinedload(Task.type),
                joinedload(PDP.tasks).joinedload(Task.status),
            )
            .where(where_option)
            .order_by(alias(task_alias, name='task_2').c.status_id)
        )

    async def get_by_user_id(
        self,
        user_id: int,
        session: AsyncSession,
    ):
        done_subquery = (
            select(func.count())
            .select_from(PDP)
            .join(task_alias, task_alias.pdp_id == PDP.id)
            .where(PDP.user_id == user_id)
            .join(status_alias, status_alias.id == task_alias.status_id)
            .where(
                status_alias.value.in_(["исполнено", "выполнено", "отменено"])
            )
            .label("done")
        )
        total_subquery = (
            select(func.count())
            .select_from(PDP)
            .join(task_alias, task_alias.pdp_id == PDP.id)
            .where(PDP.user_id == user_id)
            .label("total")
        )
        result = await self.__get_execute(
            session=session,
            where_option=PDP.user_id == user_id,
            done_subquery=done_subquery,
            total_subquery=total_subquery,
        )
        dpd_obj = result.first()
        if dpd_obj is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return self._add_statistic_to_dpd(*dpd_obj)

    async def get(
        self,
        pdp_id: int,
        session: AsyncSession,
    ):
        done_subquery = (
            select(func.count())
            .select_from(PDP)
            .join(task_alias, task_alias.pdp_id == pdp_id)
            .where(PDP.id == pdp_id)
            .join(status_alias, status_alias.id == task_alias.status_id)
            .where(
                status_alias.value.in_(["исполнено", "выполнено", "отменено"])
            )
            .label("done")
        )
        total_subquery = (
            select(func.count())
            .select_from(PDP)
            .join(task_alias, task_alias.pdp_id == pdp_id)
            .where(PDP.id == pdp_id)
            .label("total")
        )

        result = await self.__get_execute(
            session=session,
            where_option=PDP.id == pdp_id,
            done_subquery=done_subquery,
            total_subquery=total_subquery,
        )
        dpd_obj = result.first()
        if dpd_obj is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return self._add_statistic_to_dpd(*dpd_obj)

    async def get_multi_by_users(
        self, session: AsyncSession, user_ids: set[int]
    ):
        db_obj = await session.execute(
            select(self.model.id).where(self.model.user_id.in_(user_ids))
        )
        return db_obj.scalars().all()


pdp_crud = CRUDpdp(PDP)
