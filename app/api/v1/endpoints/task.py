from fastapi import APIRouter, Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.permissions import (
    is_task_owner_chief,
    is_task_owner_or_chief,
    only_chief_accesses,
)
from app.core import exceptions
from app.core.constants import (
    CHIEF_TASK_CREATE_FIELDS,
    CHIEF_TASK_UPDATE_FIELDS,
    EMPLOYEE_TASK_CREATE_FIELDS,
    EMPLOYEE_TASK_UPDATE_FIELDS,
    TASK_CREATE_EXAMPLES,
    TASK_UPDATE_EXAMPLES,
)
from app.core.db import get_async_session
from app.core.user import current_user
from app.crud.task import task_crud
from app.models import Task, User, UserRole
from app.schemas import TaskCreate, TaskRead, TaskUpdate

router = APIRouter()


@router.get(
    '/{task_id}',
    response_model=TaskRead,
    dependencies=[Depends(is_task_owner_or_chief)],
)
async def get_task(
    task_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    task_obj = await task_crud.get(task_id=task_id, session=session)
    if task_obj is None:
        raise exceptions.NotExistException(model=Task, pk=task_id)
    return task_obj


@router.post(
    '/',
    response_model=TaskRead,
)
async def create_task(
    task_in: TaskCreate = Body(openapi_examples=TASK_CREATE_EXAMPLES),
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    allowed_fields = (
        CHIEF_TASK_CREATE_FIELDS
        if user.role == UserRole.CHIEF
        else EMPLOYEE_TASK_CREATE_FIELDS
    )
    for field, value in task_in:
        if field not in allowed_fields and value is not None:
            raise exceptions.NoAccessFieldException(field=field)
    task_obj = await task_crud.create(session=session, obj_in=task_in)
    return await task_crud.get(session=session, task_id=task_obj.id)


@router.patch(
    '/{task_id}',
    response_model=TaskRead,
    dependencies=[Depends(is_task_owner_or_chief)],
)
async def change_task(
    task_id: int,
    task_in: TaskUpdate = Body(openapi_examples=TASK_UPDATE_EXAMPLES),
    session: AsyncSession = Depends(get_async_session),
    is_chief: bool = Depends(is_task_owner_chief),
):
    task_db = await task_crud.get(task_id=task_id, session=session)
    if task_db is None:
        raise exceptions.NotExistException(model=Task, pk=task_id)
    allowed_fields = (
        CHIEF_TASK_UPDATE_FIELDS if is_chief else EMPLOYEE_TASK_UPDATE_FIELDS
    )
    for field, value in task_in:
        if field not in allowed_fields and value is not None:
            raise exceptions.NoAccessFieldException(field=field)
    return await task_crud.update(
        session=session, obj_in=task_in, db_obj=task_db
    )


@router.delete(
    '/{task_id}',
    status_code=204,
    deprecated=True,
    dependencies=[
        Depends(only_chief_accesses),
        Depends(is_task_owner_or_chief),
    ],
)
async def delete_task(
    task_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    task_obj = await task_crud.get(task_id=task_id, session=session)
    if task_obj is None:
        raise exceptions.NotExistException(model=Task, pk=task_id)
    await task_crud.remove(db_obj=task_obj, session=session)
    return {'details': 'ok'}
