from typing import Generator, Iterable

from sqlalchemy import Row

from app.models import PDP, User


class StatisticMixin:
    @staticmethod
    def _add_statistic_to_dpd(pdp: PDP, done: int, total: int) -> PDP:
        pdp.__setattr__('done', done)
        pdp.__setattr__('total', total)
        return pdp

    @staticmethod
    def _add_user_statistic_generator(
        rows: Iterable[Row[tuple[User, int, int]]]
    ) -> Generator:
        for row in rows:
            user, done, total = row
            StatisticMixin._add_statistic_to_dpd(user.pdp, done, total)
            yield user
