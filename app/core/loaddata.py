import asyncio
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
import pandas as pd

from app.models.user import User
from app.core.db import engine


async def load_data(session):
    data = {
        "created": [datetime.now() for _ in range(5)],
        "first_name": ['John', 'Alice', 'Bob', 'Charlie', 'David'],
        "last_name": ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'],
        "patronymic_name": [None, None, None, None, None],
        "position": ['chief', 'employee', 'employee', 'employee', 'employee']
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
