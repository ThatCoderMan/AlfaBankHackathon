from typing import Generator, Iterable

from sqlalchemy import Row

from app.models import PDP, User


class StatisticMixin:
    @staticmethod
    def _add_statistic_to_dpd(
        pdp: PDP | None, done: int, total: int
    ) -> PDP | None:
        if pdp is None:
            return None
        pdp.__setattr__('done', done if done is not None else 0)
        pdp.__setattr__('total', total if total is not None else 0)
        return pdp

    @staticmethod
    def _add_user_statistic_generator(
        rows: Iterable[Row[tuple[User, int, int]]]
    ) -> Generator:
        for row in rows:
            user, done, total = row
            StatisticMixin._add_statistic_to_dpd(user.pdp, done, total)
            yield user
