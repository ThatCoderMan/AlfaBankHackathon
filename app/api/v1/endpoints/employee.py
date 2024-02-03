from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.permissions import only_chief_accesses
from app.core.db import get_async_session
from app.core.exceptions import Error403Schema, ErrorSchema
from app.crud import user_crud
from app.models import User
from app.schemas import UserShort

router = APIRouter()


@router.get(
    '/employees',
    response_model_exclude={'is_active'},
    responses={
        200: {'model': list[UserShort]},
        401: {'model': ErrorSchema},
        403: {'model': Error403Schema},
    },
)
async def get_employees(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(only_chief_accesses),
):
    data = await user_crud.get_employees(session=session, user_id=user.id)
    return data
