from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import get_or_404, only_chief
from app.core.db import get_async_session
from app.core.user import current_user
from app.crud.task import task_crud
from app.models import User
from app.schemas import TaskCreate, TaskRead, TaskUpdate

router = APIRouter()


@router.get('/{task_id}', response_model=TaskRead)
async def get_task(
    task_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(only_chief)
):
    return await task_crud.get(task_id=task_id, session=session)


@router.post('/', response_model=TaskRead)
async def create_task(
    task_in: TaskCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    task_obj_in = await get_or_404(task_in, session=session)
    task_obj = await task_crud.create(session=session, obj_in=task_obj_in)
    return await task_crud.get(session=session, task_id=task_obj.id)


@router.patch(
    '/{task_id}',
    response_model=TaskRead,
)
async def change_task(
    task_id: int,
    task_in: TaskUpdate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    task_db = await task_crud.get(task_id=task_id, session=session)
    return await task_crud.update(
        session=session, obj_in=task_in, db_obj=task_db
    )
