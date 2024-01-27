from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user
from app.crud import pdp_crud, user_crud
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


async def is_pdp_owner(
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
            status_code=404, detail='ИПР с id {pdp_id} не существует')
    pdp_owner = user_crud.get(session=session, obj_id=pdp.user_id)
    if pdp_owner.chief_id != user.id and pdp.user_id != user.id:
        raise HTTPException(
            status_code=403, detail='Доступ к чужим ИПР запрещен')
    return pdp
