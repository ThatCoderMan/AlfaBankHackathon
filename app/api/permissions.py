from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.exceptions import NoAccessByUserException
from app.core.user import current_user
from app.crud import pdp_crud, task_crud, user_crud
from app.models import User, UserRole


def only_chief_accesses(user: User = Depends(current_user)):
    if user.role != UserRole.CHIEF:
        raise NoAccessByUserException(email=user.email)
    return user


async def is_pdp_owner_or_chief(
    pdp_id: int,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    pdp = await pdp_crud.get(session=session, pdp_id=pdp_id)
    is_chief = await user_crud.is_chief(
        session=session, chief_id=user.id, user_id=pdp.user_id)
    if not is_chief and pdp.user_id != user.id:
        raise NoAccessByUserException(email=user.email)

    return pdp


async def is_pdp_owner_chief(
    pdp_id: int,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    pdp = await pdp_crud.get(session=session, pdp_id=pdp_id)
    is_chief = await user_crud.is_chief(
        session=session, chief_id=user.id, user_id=pdp.user_id)
    if not is_chief:
        raise NoAccessByUserException(email=user.email)
    return pdp


async def is_task_owner_or_chief(
    task_id: int,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    task = await task_crud.get(session=session, task_id=task_id)
    pdp = await pdp_crud.get(session=session, pdp_id=task.pdp_id)
    is_chief = await user_crud.is_chief(
        session=session, chief_id=user.id, user_id=pdp.user_id)
    if not is_chief and pdp.user_id != user.id:
        raise NoAccessByUserException(email=user.email)
    return task


async def is_task_owner_chief(
    task_id: int,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    task = await task_crud.get(session=session, task_id=task_id)
    pdp = await pdp_crud.get(session=session, pdp_id=task.pdp_id)
    return await user_crud.is_chief(
        session=session, chief_id=user.id, user_id=pdp.user_id)
