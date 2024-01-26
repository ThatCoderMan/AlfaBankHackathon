from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.permissions import only_chief_accesses, is_task_owner_or_chief
from app.core.db import get_async_session
from app.core.user import current_user
from app.crud.task import task_crud
from app.schemas import TaskCreate, TaskRead, TaskUpdate

router = APIRouter()


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


# Todo: Проверка полей редактирования в зависимости от роли.
@router.patch(
    '/{task_id}',
    response_model=TaskRead,
    dependencies=[Depends(only_chief_accesses)])
async def change_task(
        task_id: int,
        task_in: TaskUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    task_db = await task_crud.get(task_id=task_id, session=session)
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
