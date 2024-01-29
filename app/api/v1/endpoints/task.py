from typing import Optional, Union

from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.permissions import is_task_owner_or_chief, is_task_owner_chief
from app.core.db import get_async_session
from app.core.user import current_user
from app.crud.task import task_crud
from app.models import User
from app.schemas import TaskCreate, TaskRead, TaskUpdate

router = APIRouter()


task_update_examples = [{
    "type_id": 1,
    "status_id": 1,
    'title': "string",
    "description": "string",
    "skills": [{"id": 1, },],
    "link": "string",
    "chief_comment": "string",
    "starting_date": "string",
    "deadline": "string",
},
    {
    "status_id": 1,
    "employee_comment": "string",

},

]

# Todo: permission У текущего пользователя есть доступ к задаче
#  (шеф или сотрудник) таск_id == user_id and role == chief где его сотрудники


@router.get(
    '/{task_id}',
    response_model=TaskRead,
    dependencies=[Depends(current_user), Depends(is_task_owner_or_chief)]
)
async def get_task(
        task_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    return await task_crud.get(task_id=task_id, session=session)


# Todo: проверка полей при создании руководителем,
#  или сотрудником, меняются поля создания задачи
@router.post(
    '/',
    response_model=TaskRead,
    dependencies=[Depends(current_user), Depends(is_task_owner_or_chief)]
)
async def create_task(
        task_in: TaskCreate,
        session: AsyncSession = Depends(get_async_session),
):
    task_obj = await task_crud.create(session=session, obj_in=task_in)
    return await task_crud.get(session=session, task_id=task_obj.id)


async def schemes(user: User = Depends(current_user)):
    if user.role == 'chief':
        return True
    return False

# Todo: Проверка полей редактирования в зависимости от роли.


@router.patch(
    '/{task_id}',
    response_model=TaskRead,
    dependencies=[Depends(is_task_owner_or_chief)])
async def change_task(
        task_id: int,
        task_in: TaskUpdate,
        session: AsyncSession = Depends(get_async_session),
        is_task_owner_chief: bool = Depends(is_task_owner_chief),
):
    task_db = await task_crud.get(task_id=task_id, session=session)
    if not is_task_owner_chief:
        allowed_fields = {'employee_comment', 'status_id'}
        for field in task_in:
            if field not in allowed_fields:
                raise HTTPException(status_code=403, detail="Forbidden")
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
