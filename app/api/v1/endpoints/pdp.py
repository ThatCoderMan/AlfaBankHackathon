from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.permissions import is_pdp_owner_chief, is_pdp_owner_or_chief
from app.core import exceptions
from app.core.db import get_async_session
from app.core.exceptions import Error403Schema, ErrorSchema
from app.core.user import current_user
from app.crud import pdp_crud
from app.models import PDP, User
from app.schemas import PDPRead, PDPUpdate

router = APIRouter()


@router.get(
    '/my',
    responses={
        200: {'model': PDPRead},
        401: {'model': ErrorSchema},
        404: {'model': ErrorSchema},
    },
)
async def get_my_pdp(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    pdp_obj = await pdp_crud.get_by_user_id(session=session, user_id=user.id)
    if pdp_obj is None:
        raise exceptions.NotExistException(model=PDP)
    return pdp_obj


@router.get(
    '/{pdp_id}',
    dependencies=[Depends(current_user), Depends(is_pdp_owner_or_chief)],
    responses={
        200: {'model': PDPRead},
        401: {'model': ErrorSchema},
        404: {'model': ErrorSchema},
    },
)
async def get_pdp(
    pdp_id: int, session: AsyncSession = Depends(get_async_session)
):
    pdp_obj = await pdp_crud.get(session=session, pdp_id=pdp_id)
    if pdp_obj is None:
        raise exceptions.NotExistException(model=PDP, pk=pdp_id)
    return pdp_obj


@router.patch(
    '/{pdp_id}',
    dependencies=[Depends(is_pdp_owner_chief)],
    responses={
        200: {'model': PDPRead},
        401: {'model': ErrorSchema},
        403: {'model': Error403Schema},
        404: {'model': ErrorSchema},
    },
)
async def change_pdp(
    pdp_id: int,
    pdp_in: PDPUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    pdp_db = await pdp_crud.get(session=session, pdp_id=pdp_id)
    if pdp_db is None:
        raise exceptions.NotExistException(model=PDP, pk=pdp_id)
    data = await pdp_crud.update(session=session, db_obj=pdp_db, obj_in=pdp_in)
    return data
