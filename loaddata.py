import asyncio
from datetime import datetime

from fastapi_users.password import PasswordHelper
from sqlalchemy.ext.asyncio import AsyncSession
import pandas as pd

from app.core.db import engine
from app.models import User

password = PasswordHelper()


async def load_data(session):
    data = {
        'email': ['john@example.com', 'alice@example.com', 'bob@example.com',
                  'charlie@example.com', 'david@example.com'],
        'is_active': [True, True, True, True, True],
        'is_superuser': [False, False, False, False, False],
        'is_verified': [False, False, False, False, False],
        'created': [datetime.now() for _ in range(5)],
        'first_name': ['John', 'Alice', 'Bob', 'Charlie', 'David'],
        'last_name': ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'],
        'patronymic_name': ['string', 'string', 'string', 'string', 'string'],
        'position': ['string', 'string', 'string', 'string', 'string'],
        'role': ['chief', 'employee', 'employee', 'employee', 'employee'],
        'photo': ['string', 'string', 'string', 'string', 'string'],
        'hashed_password': [password.hash('string') for _ in range(5)],
    }

    df = pd.DataFrame(data)

    for _, row in df.iterrows():
        user = User(**row)
        session.add(user)
    await session.commit()


async def main():
    async with AsyncSession(engine) as session:
        await load_data(session)


asyncio.run(main())
