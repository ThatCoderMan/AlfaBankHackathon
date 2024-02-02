import asyncio
from datetime import datetime, timedelta
from typing import AsyncGenerator

import pytest
from fastapi_users.password import PasswordHelper
from httpx import AsyncClient
from sqlalchemy import NullPool, insert
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.db import Base, get_async_session
from app.main import app
from app.models import Direction, Grade, PDP, Skill, Status, Task, Type, User
from app.models.user import user_user
from tests import constants

SQLALCHEMY_DATABASE_URL_TEST = 'postgresql+asyncpg://postgres:admin@127.0.0.1:5432/postgres_tests_alfa'  # noqa

engine_test = create_async_engine(SQLALCHEMY_DATABASE_URL_TEST,
                                  poolclass=NullPool)

async_session_marker = sessionmaker(engine_test,
                                    class_=AsyncSession,
                                    expire_on_commit=False)

Base.bind = engine_test


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_marker() as session:
        yield session


app.dependency_overrides[get_async_session] = override_get_async_session


@pytest.fixture(autouse=True, scope='session')
async def create_db():
    """Создание Таблиц в Базе Данных."""
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope='session')
async def custom_event_loop(request):
    """Создание экземпляра цикла событий по умолчанию
     для каждого тестового примера."""
    loop = asyncio.set_event_loop(asyncio.new_event_loop())  # noqa

    yield loop


@pytest.fixture(scope='session')
async def async_client(custom_event_loop) -> AsyncGenerator[AsyncClient, None]:
    """Создание Асинхронного Клиента."""
    async with AsyncClient(app=app, base_url='http://test') as ac:
        yield ac


async def create_fixture(session_marker, model, data):
    async with session_marker() as session:
        for num, value in enumerate(data, start=1):
            test_data = insert(model).values(
                id=num,
                value=value
            )
            await session.execute(test_data)
            await session.commit()

    return model


@pytest.fixture(scope='session')
async def fixture_directions():
    return await create_fixture(async_session_marker, Direction,
                                constants.directions)


@pytest.fixture(scope='session')
async def fixture_grade():
    return await create_fixture(async_session_marker, Grade, constants.grade)


@pytest.fixture(scope='session')
async def fixture_skill():
    return await create_fixture(async_session_marker, Skill, constants.skill)


@pytest.fixture(scope='session')
async def fixture_type():
    return await create_fixture(async_session_marker, Type, constants.types)


@pytest.fixture(scope='session')
async def fixture_status():
    async with async_session_marker() as session:
        for num, (value, role) in enumerate(
                zip(constants.status, constants.roles), start=1):
            test_data = insert(Status).values(
                id=num,
                role=role,
                value=value
            )
            await session.execute(test_data)
            await session.commit()

    return Status


@pytest.fixture(scope='session')
async def fixture_users():
    async with async_session_marker() as session:
        password = PasswordHelper()
        for num, values in enumerate(constants.users_data, start=1):
            email, role, position = values.split(' ')
            test_data = insert(User).values(
                id=num,
                created=datetime.now(),
                email=email,
                is_active=True,
                is_superuser=False,
                is_verified=False,
                first_name=f'User{role}',
                last_name=f'User{num}',
                patronymic_name='string',
                position=position,
                role=role,
                photo='string',
                hashed_password=password.hash('password'),
            )
            await session.execute(test_data)
            await session.commit()

    return User


@pytest.fixture(scope='session')
async def fixture_pdp(fixture_users):
    async with async_session_marker() as session:
        test_data = insert(PDP).values(
            id=1,
            user_id=2,
            goal='Finish',
            starting_date=datetime.now(),
            deadline=datetime.now() + timedelta(days=365),
        )
        await session.execute(test_data)
        await session.commit()

    return PDP


@pytest.fixture(scope='session')
async def fixture_task(fixture_directions, fixture_grade, fixture_pdp,
                       fixture_skill, fixture_status, fixture_type):
    async with async_session_marker() as session:
        test_data = insert(Task).values(
            id=10,
            pdp_id=1,
            type_id=1,
            status_id=1,
            title='Title',
            description='Description',
            link='http://link',
            starting_date=datetime.now(),
            deadline=datetime.now() + timedelta(days=365),
        )
        await session.execute(test_data)
        await session.commit()

    return Task


@pytest.fixture(scope='session')
async def fixture_user_user(fixture_users):
    async with async_session_marker() as session:
        test_data = insert(user_user).values(
            user_id=2,
            chief_id=1
        )
        await session.execute(test_data)
        await session.commit()

    return user_user
