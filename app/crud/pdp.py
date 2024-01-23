from sqlalchemy import alias, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import aliased, joinedload

from app.models import PDP, Status, Task

from .base import CRUDBase


class CRUDpdp(CRUDBase):
    @staticmethod
    def _add_statistic(pdp: PDP, done: int, total: int) -> PDP:
        pdp.__setattr__('done', done)
        pdp.__setattr__('total', total)
        return pdp

    async def get_by_user_id(
        self,
        user_id: int,
        session: AsyncSession,
    ):
        status_alias = aliased(Status)
        task_alias = aliased(Task)

        done_subquery = (
            select(func.count())
            .select_from(PDP)
            .join(task_alias, task_alias.pdp_id == PDP.id)
            .where(self.model.user_id == user_id)
            .join(status_alias, status_alias.id == task_alias.status_id)
            .where(
                status_alias.name.in_(["исполнено", "выполнено", "отменено"])
            )
            .label("done")
        )
        total_subquery = (
            select(func.count())
            .select_from(PDP)
            .join(task_alias, task_alias.pdp_id == PDP.id)
            .where(self.model.user_id == user_id)
            .label("total")
        )
        db_obj = await session.execute(
            select(self.model, done_subquery, total_subquery)
            .options(joinedload(PDP.tasks))
            .options(
                joinedload(PDP.tasks).joinedload(Task.type),
                joinedload(PDP.tasks).joinedload(Task.status),
            )
            .where(self.model.user_id == user_id)
            .order_by(alias(task_alias, name='task_2').c.status_id)
        )
        row = db_obj.first()
        return self._add_statistic(*row)

    async def get(
        self,
        pdp_id: int,
        session: AsyncSession,
    ):
        status_alias = aliased(Status)
        task_alias = aliased(Task)

        done_subquery = (
            select(func.count())
            .select_from(PDP)
            .join(task_alias, task_alias.pdp_id == pdp_id)
            .where(self.model.id == pdp_id)
            .join(status_alias, status_alias.id == task_alias.status_id)
            .where(
                status_alias.name.in_(["исполнено", "выполнено", "отменено"])
            )
            .label("done")
        )
        total_subquery = (
            select(func.count())
            .select_from(PDP)
            .join(task_alias, task_alias.pdp_id == pdp_id)
            .where(self.model.id == pdp_id)
            .label("total")
        )
        db_obj = await session.execute(
            select(self.model, done_subquery, total_subquery)
            .options(joinedload(PDP.tasks))
            .options(
                joinedload(PDP.tasks).joinedload(Task.type),
                joinedload(PDP.tasks).joinedload(Task.status),
            )
            .where(self.model.id == pdp_id)
            .order_by(alias(task_alias, name='task_2').c.status_id)
        )
        row = db_obj.first()
        return self._add_statistic(*row)


pdp_crud = CRUDpdp(PDP)
