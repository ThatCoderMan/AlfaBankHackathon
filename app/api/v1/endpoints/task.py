from fastapi import APIRouter, BackgroundTasks, Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.permissions import (
    is_task_owner_chief,
    is_task_owner_or_chief,
    only_chief_accesses,
)
from app.core import exceptions
from app.core.constants import (
    APPLICATION_STATUS_ID,
    AT_WORK_STATUS_ID,
    CHIEF_TASK_CREATE_FIELDS,
    CHIEF_TASK_UPDATE_FIELDS,
    EMPLOYEE_TASK_CREATE_FIELDS,
    EMPLOYEE_TASK_UPDATE_FIELDS,
    TASK_CREATE_EXAMPLES,
    TASK_UPDATE_EXAMPLES,
)
from app.core.db import get_async_session
from app.core.user import current_user
from app.crud import pdp_crud, status_crud, task_crud
from app.models import Task, User, UserRole
from app.schemas import TaskCreate, TaskRead, TaskUpdate
from app.services.email import change_task_email, new_post_task

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
    background_tasks: BackgroundTasks,
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
    task_in.status_id = AT_WORK_STATUS_ID
    if user.role == UserRole.EMPLOYEE:
        pdp = await pdp_crud.get_by_user_id(session=session, user_id=user.id)
        task_in.pdp_id = pdp.id
        task_in.status_id = APPLICATION_STATUS_ID
        task_in.skills = ['default']
    task_obj = await task_crud.create(session=session, obj_in=task_in)

    await session.refresh(user)

    result = await task_crud.get(session=session, task_id=task_obj.id)

    data_email = {
        'user': user,
        'task': result,
    }
    background_tasks.add_task(new_post_task, data_email)
    return result


@router.patch(
    '/{task_id}',
    response_model=TaskRead,
    dependencies=[Depends(is_task_owner_or_chief)],
)
async def change_task(
    background_tasks: BackgroundTasks,
    task_id: int,
    task_in: TaskUpdate = Body(openapi_examples=TASK_UPDATE_EXAMPLES),
    session: AsyncSession = Depends(get_async_session),
    is_chief: bool = Depends(is_task_owner_chief),
    user: User = Depends(current_user),
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
    statuses = await status_crud.get_multi_by_role(session=session, user=user)
    if user.role == UserRole.EMPLOYEE:
        if (
            task_in.status_id not in [status.id for status in statuses]
            or task_in.status_id == APPLICATION_STATUS_ID
        ):
            raise exceptions.UnacceptableStatusException(
                status_id=task_in.status_id
            )
    else:
        if (
            task_in.status_id not in [status.id for status in statuses]
            or task_in.status_id == AT_WORK_STATUS_ID
        ):
            raise exceptions.UnacceptableStatusException(
                status_id=task_in.status_id
            )

    old_status = task_db.status.value
    old_chief_comment = task_db.chief_comment
    old_employee_comment = task_db.employee_comment
    result = await task_crud.update(
        session=session, obj_in=task_in, db_obj=task_db
    )
    await session.refresh(user)

    data_email = {
        'user': user,
        'old_status': old_status,
        'old_chief_comment': old_chief_comment,
        'old_employee_comment': old_employee_comment,
        'task': result,
    }
    background_tasks.add_task(change_task_email, data_email)
    return result


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
