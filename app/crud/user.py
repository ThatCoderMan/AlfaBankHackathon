from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import aliased, joinedload

from app.models import PDP, Status, Task, Template, User
from app.models.user import user_user

from .base import CRUDBase
from .mixin import StatisticMixin


class CRUDUser(CRUDBase, StatisticMixin):
    async def get_templates_creators(self, session: AsyncSession):
        db_objs = await session.execute(
            select(self.model).join(Template, Template.user_id == User.id)
        )
        return db_objs.scalars().unique()

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
            .where(status_alias.value.in_(["Исполнено", "Выполнено"]))
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

    async def is_chief(
        self, session: AsyncSession, user_id: int, chief_id: int
    ):
        is_chief = await session.execute(
            user_user.select().where(
                user_user.c.user_id == user_id,
                user_user.c.chief_id == chief_id,
            )
        )
        return bool(is_chief.scalars().first())

    async def get_email_chief(self, user, session):
        db_obj = await session.execute(
            select(self.model)
            .join(user_user, user_user.c.chief_id == User.id)
            .where(user_user.c.user_id == user.id)
            .options(joinedload(User.pdp))
        )

        return db_obj.scalar()

    async def get_email_employee(self, user, session):
        db_obj = await session.execute(
            select(self.model)
            .join(user_user, user_user.c.user_id == User.id)
            .where(user_user.c.chief_id == user.id)
            .options(joinedload(User.pdp))
        )

        return db_obj.scalar()


user_crud = CRUDUser(User)
