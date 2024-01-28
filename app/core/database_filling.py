import asyncio
from random import choice
from typing import Literal

from faker import Faker
from fastapi_users.password import PasswordHelper
from sqlalchemy import delete, insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import AsyncSessionLocal
from app.models import (
    PDP,
    Direction,
    Grade,
    Status,
    Task,
    Template,
    Type,
    User,
)

fake = Faker()
fake_ru = Faker('ru_RU')


async def clear_db(session: AsyncSession, model):
    stmt = delete(model)
    await session.execute(stmt)
    await session.commit()


async def insert_value_data(session: AsyncSession, model, data):
    for i, item in enumerate(data, start=1):
        stmt = insert(model).values({'id': i, 'value': item})
        await session.execute(stmt)
    await session.commit()


async def insert_types(session: AsyncSession):
    types = [
        "Иное",
        "Внутренний курс",
        "Внешний курс",
        "Менторство",
        "Наставничество",
        "Самостоятельное обучение",
    ]
    await insert_value_data(session, Type, types)


async def insert_grades(session: AsyncSession):
    grades = ["не определен", "Junior", "Middle", "Senior"]
    await insert_value_data(session, Grade, grades)


async def insert_directions(session: AsyncSession):
    directions = [
        "не определен",
        "Дизайн",
        "Delivery Менеджмент",
        "ВА аналитика",
        "SA аналитика",
        "Программирование",
        "Discovery менеджмент",
        "Soft Skills",
        "Маркетинг",
    ]
    await insert_value_data(session, Direction, directions)


async def insert_users(
    session: AsyncSession,
    count: int,
    role: Literal['CHIEF', 'EMPLOYEE'],
    start_ind=1,
):
    for id in range(start_ind, count + start_ind):
        name = fake.name()
        stmt = insert(User).values(
            {
                'id': id,
                'first_name': name.split()[0],
                'last_name': name.split()[1]
                if len(name.split()) > 1
                else fake.suffix(),
                'patronymic_name': fake.suffix(),
                'position': fake.job(),
                'role': role,
                'photo': fake.image_url(),
                'email': fake.email(),
                'hashed_password': PasswordHelper().hash('string'),
            }
        )
        await session.execute(stmt)
    await session.commit()


async def insert_tasks(session: AsyncSession, count: int, pdp=list[int]):
    for _ in range(1, count + 1):
        stmt = insert(Task).values(
            {
                'title': fake.sentence(),
                'description': fake.paragraph(),
                'link': fake.url(),
                'starting_date': fake.date_this_year(),
                'deadline': fake.date_between(
                    start_date='+30d', end_date='next_year'
                ),
                'chief_comment': choice([fake.text(), None]),
                'employee_comment': choice([fake.text(), None]),
            }
        )
        await session.execute(stmt)
    await session.commit()


async def insert_pdps(session: AsyncSession, count: int):
    for id in range(1, count + 1):
        goal = fake.sentence()

        stmt = insert(PDP).values(
            {
                'id': id,
                'goal': goal,
                'starting_date': fake.date_this_year(),
                'deadline': fake.date_between(
                    start_date='+30d', end_date='next_year'
                ),
            }
        )
        await session.execute(stmt)
    await session.commit()


async def insert_templates(session: AsyncSession, count: int):
    for id in range(1, count + 1):
        title = fake.sentence()
        description = fake.paragraph()

        stmt = insert(Template).values(
            {
                'id': id,
                'title': title,
                'description': description,
                'duration': fake.random_int(min=1, max=366),
                'recommendation': fake.text(),
                'link': fake.url(),
            }
        )
        await session.execute(stmt)
    await session.commit()


async def insert_statuses(session: AsyncSession):
    statuses = [
        ("В работе", "CHIEF"),
        ("Выполнена", "CHIEF"),
        ("Отменена", "CHIEF"),
        ("Запланирована", "CHIEF"),
        ("Исполнена", "EMPLOYEE"),
        ("Заявка", "EMPLOYEE"),
    ]
    for i, (status, role) in enumerate(statuses, start=1):
        stmt = insert(Status).values({'id': i, 'value': status, 'role': role})
        await session.execute(stmt)
    await session.commit()


async def main():
    async with AsyncSessionLocal() as session:
        for model in [Type, Status, Direction, Grade]:
            await clear_db(session, model)
        await insert_types(session)
        await insert_statuses(session)
        await insert_directions(session)
        await insert_grades(session)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
