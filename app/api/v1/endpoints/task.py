from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user
from app.models import User
from app.schemas import TaskCreate, TaskRead, TaskUpdate

router = APIRouter()


@router.get('/{task_id}', response_model=TaskRead)
async def get_task(
    pdp_id: int,
    task_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return {None}


@router.post('/{task_id}', response_model=TaskRead)
async def create_task(
    pdp_id: int,
    task_id: int,
    task_obj: TaskCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return {None}


@router.patch(
    '/{task_id}',
    response_model=TaskRead,
)
async def change_task(
    pdp_id: int,
    task_id: int,
    task_obj: TaskUpdate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return {None}
