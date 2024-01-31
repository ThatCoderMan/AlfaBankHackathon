from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.permissions import is_task_owner_or_chief, is_task_owner_chief
from app.core.constants import (
    CHIEF_TASK_CREATE_FIELDS,
    CHIEF_TASK_UPDATE_FIELDS,
    EMPLOYEE_TASK_CREATE_FIELDS,
    EMPLOYEE_TASK_UPDATE_FIELDS,
    INSUFFICIENT_PERMISSIONS_FOR_FIELD_FILL,
    INSUFFICIENT_PERMISSIONS_FOR_FIELD_UPDATE,
    TASK_CREATE_EXAMPLES,
    TASK_UPDATE_EXAMPLES
)
from app.core.db import get_async_session
from app.core.user import current_user
from app.crud.task import task_crud
from app.models import User, UserRole
from app.schemas import TaskCreate, TaskRead, TaskUpdate

router = APIRouter()


@router.get(
    '/{task_id}',
    response_model=TaskRead,
    dependencies=[
        Depends(current_user),
        Depends(is_task_owner_or_chief)]
)
async def get_task(
        task_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    return await task_crud.get(task_id=task_id, session=session)


@router.post(
    '/',
    response_model=TaskRead,
    dependencies=[Depends(current_user)]
)
async def create_task(
        task_in: TaskCreate = Body(openapi_examples=TASK_CREATE_EXAMPLES),
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    if user.role != UserRole.CHIEF:
        allowed_fields = EMPLOYEE_TASK_CREATE_FIELDS
    else:
        allowed_fields = CHIEF_TASK_CREATE_FIELDS
    for field in task_in:
        if field[0] not in allowed_fields and field[1] is not None:
            raise HTTPException(
                status_code=403,
                detail=INSUFFICIENT_PERMISSIONS_FOR_FIELD_FILL.format(
                    field=field[0]
                )
            )
    task_obj = await task_crud.create(session=session, obj_in=task_in)
    return await task_crud.get(session=session, task_id=task_obj.id)


@router.patch(
    '/{task_id}',
    response_model=TaskRead,
    dependencies=[
        Depends(current_user),
        Depends(is_task_owner_or_chief)
    ])
async def change_task(
        task_id: int,
        task_in: TaskUpdate = Body(openapi_examples=TASK_UPDATE_EXAMPLES),
        session: AsyncSession = Depends(get_async_session),
        is_task_owner_chief: bool = Depends(is_task_owner_chief),
):
    task_db = await task_crud.get(task_id=task_id, session=session)
    if not is_task_owner_chief:
        allowed_fields = EMPLOYEE_TASK_UPDATE_FIELDS
    else:
        allowed_fields = CHIEF_TASK_UPDATE_FIELDS
    for field in task_in:
        if field[0] not in allowed_fields and field[1] is not None:
            raise HTTPException(
                status_code=403,
                detail=INSUFFICIENT_PERMISSIONS_FOR_FIELD_UPDATE.format(
                    field=field[0]
                )
            )
    return await task_crud.update(
        session=session, obj_in=task_in, db_obj=task_db
    )


@router.delete('/{task_id}', status_code=204, deprecated=True)
async def delete_task(
    task_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    template_obj = await task_crud.get(task_id=task_id, session=session)
    await task_crud.remove(db_obj=template_obj, session=session)
    return {'message': 'ok'}
