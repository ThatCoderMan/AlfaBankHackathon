from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.constants import (
    INSUFFICIENT_PERMISSIONS_FOR_ACTION,
    NO_ACCESS_PDP_MESSAGE,
    NO_ACCESS_TASK_MESSAGE,
    NOT_EXIST_PDP_MESSAGE,
    NOT_EXIST_TASK_MESSAGE
)
from app.core.db import get_async_session
from app.core.user import current_user
from app.crud import pdp_crud, task_crud, user_crud
from app.models import User, UserRole


def only_chief_accesses(user: User = Depends(current_user)):
    if user.role != UserRole.CHIEF:
        raise HTTPException(
            status_code=403,
            detail=INSUFFICIENT_PERMISSIONS_FOR_ACTION.format(email=user.email)
        )
    return user


async def is_pdp_owner_or_chief(
    pdp_id: int,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    pdp = await pdp_crud.get(session=session, pdp_id=pdp_id)
    if pdp is None:
        raise HTTPException(
            status_code=404, detail=NOT_EXIST_PDP_MESSAGE.format(pdp_id=pdp_id)
        )
    is_chief = await user_crud.is_chief(
        session=session, chief_id=user.id, user_id=pdp.user_id)
    if not is_chief and pdp.user_id != user.id:
        raise HTTPException(
            status_code=403, detail=NO_ACCESS_PDP_MESSAGE)
    return pdp


async def is_pdp_owner_chief(
    pdp_id: int,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    pdp = await pdp_crud.get(session=session, pdp_id=pdp_id)
    if pdp is None:
        raise HTTPException(
            status_code=404, detail=NOT_EXIST_PDP_MESSAGE.format(pdp_id=pdp_id)
        )
    is_chief = await user_crud.is_chief(
        session=session, chief_id=user.id, user_id=pdp.user_id)
    if not is_chief:
        raise HTTPException(
            status_code=403, detail=NO_ACCESS_PDP_MESSAGE)
    return pdp


async def is_task_owner_or_chief(
    task_id: int,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    task = await task_crud.get(session=session, task_id=task_id)
    pdp = await pdp_crud.get(session=session, pdp_id=task.pdp_id)
    if task is None:
        raise HTTPException(
            status_code=404,
            detail=NOT_EXIST_TASK_MESSAGE.format(task_id=task_id)
        )
    is_chief = await user_crud.is_chief(
        session=session, chief_id=user.id, user_id=pdp.user_id)
    if not is_chief and pdp.user_id != user.id:
        raise HTTPException(
            status_code=403,
            detail=NO_ACCESS_TASK_MESSAGE
        )
    return task


async def is_task_owner_chief(
    task_id: int,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    task = await task_crud.get(session=session, task_id=task_id)
    pdp = await pdp_crud.get(session=session, pdp_id=task.pdp_id)
    if task is None:
        raise HTTPException(
            status_code=404,
            detail=NOT_EXIST_TASK_MESSAGE.format(task_id=task_id)
        )
    return await user_crud.is_chief(
        session=session, chief_id=user.id, user_id=pdp.user_id)
