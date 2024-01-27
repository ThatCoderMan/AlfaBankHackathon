from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.permissions import is_pdp_owner_or_chief
from app.core.db import get_async_session
from app.core.user import current_user
from app.crud import pdp_crud
from app.models import User
from app.schemas import PDPRead, PDPUpdate

router = APIRouter()


@router.get(
    '/my',
    response_model=PDPRead,
)
async def get_my_pdp(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    data = await pdp_crud.get_by_user_id(session=session, user_id=user.id)
    return data


# Todo : Руководитель и его сторудник
@router.get(
    '/{pdp_id}',
    response_model=PDPRead,
    dependencies=[Depends(current_user), Depends(is_pdp_owner_or_chief)]
)
async def get_pdp(
    pdp_id: int, session: AsyncSession = Depends(get_async_session)
):
    data = await pdp_crud.get(session=session, pdp_id=pdp_id)
    return data

# Todo : Руководитель и его сторудник


@router.patch(
    '/{pdp_id}',
    response_model=PDPRead,
    dependencies=[Depends(current_user), Depends(is_pdp_owner_or_chief)]
)
async def change_pdp(
    pdp_id: int,
    pdp_in: PDPUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    pdp_db = await pdp_crud.get(session=session, pdp_id=pdp_id)
    data = await pdp_crud.update(session=session, db_obj=pdp_db, obj_in=pdp_in)
    return data
