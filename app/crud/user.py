from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import aliased, joinedload

from app.models import PDP, Status, Task, User
from app.models.user import user_user

from .base import CRUDBase
from .mixin import StatisticMixin


class CRUDUser(CRUDBase, StatisticMixin):
    async def get_employees(
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
            .where(PDP.user_id == user_user.c.user_id)
            .join(user_user, user_user.c.user_id == User.id)
            .where(user_user.c.chief_id == user_id)
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
            .where(PDP.user_id == user_user.c.user_id)
            .join(user_user, user_user.c.user_id == User.id)
            .where(user_user.c.chief_id == user_id)
            .group_by(self.model)
            .label("total")
        )
        db_obj = await session.execute(
            select(self.model, done_subquery, total_subquery)
            .join(user_user, user_user.c.user_id == User.id)
            .where(user_user.c.chief_id == user_id)
            .options(joinedload(User.pdp))
        )
        users = db_obj.all()
        return list(self._add_user_statistic_generator(users))


user_crud = CRUDUser(User)
