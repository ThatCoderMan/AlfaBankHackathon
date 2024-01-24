from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user
from app.models import Status, Type, User
from app.schemas import StatusRead, TypeRead

router = APIRouter()


@router.get(
    '/statuses',
    response_model=list[StatusRead],
)
async def get_status(
    session: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(current_user),
):
    statuses = await session.execute(
        select(Status).where(Status.role == current_user.role)
    )
    return statuses.scalars().all()


@router.get(
    '/types',
    response_model=list[TypeRead],
)
async def get_type_of_task(
    session: AsyncSession = Depends(get_async_session),
):
    types = await session.execute(select(Type))
    return types.scalars().all()
