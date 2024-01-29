from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user
from app.crud import pdp_crud, task_crud, user_crud
from app.models import User
from app.models.user import UserRole


def only_chief_accesses(user: User = Depends(current_user)):
    if user.role != UserRole.CHIEF:
        raise HTTPException(
            status_code=403,
            detail=f'У пользователя {user.email} '
            f'Недостаточно прав для выполнения действия'
        )
    return user


async def is_pdp_owner_or_chief(
    pdp_id: int,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    if user.id is None:
        raise HTTPException(
            status_code=401,
            detail='Недоступно неавторизованным пользователям'
        )
    pdp = await pdp_crud.get(session=session, pdp_id=pdp_id)
    if pdp is None:
        raise HTTPException(
            status_code=404,
            detail=f'ИПР с id {pdp_id} не существует'
        )
    is_chief = await user_crud.is_chief(
        session=session, chief_id=user.id, user_id=pdp.user_id)
    if not is_chief and pdp.user_id != user.id:
        raise HTTPException(
            status_code=403,
            detail='Недостаточно прав для доступа к этому ИПР'
        )
    return pdp


async def is_task_owner_or_chief(
    task_id: int,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    if user.id is None:
        raise HTTPException(
            status_code=401,
            detail='Недоступно неавторизованным пользователям'
        )
    task = await task_crud.get(session=session, task_id=task_id)
    pdp = await pdp_crud.get(session=session, pdp_id=task.pdp_id)
    if task is None:
        raise HTTPException(
            status_code=404,
            detail=f'задача с id {task_id} не существует'
        )
    is_chief = await user_crud.is_chief(
        session=session, chief_id=user.id, user_id=pdp.user_id)
    if not is_chief and pdp.user_id != user.id:
        raise HTTPException(
            status_code=403,
            detail='Недостаточно прав для доступа к этой задаче'
        )
    return task


async def is_task_owner_chief(
    task_id: int,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    if user.id is None:
        raise HTTPException(
            status_code=401,
            detail='Недоступно неавторизованным пользователям'
        )
    task = await task_crud.get(session=session, task_id=task_id)
    pdp = await pdp_crud.get(session=session, pdp_id=task.pdp_id)
    if task is None:
        raise HTTPException(
            status_code=404,
            detail=f'задача с id {task_id} не существует'
        )
    return await user_crud.is_chief(
        session=session, chief_id=user.id, user_id=pdp.user_id)
