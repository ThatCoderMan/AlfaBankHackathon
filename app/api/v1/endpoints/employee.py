from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.permissions import only_chief_accesses
from app.core.db import get_async_session
from app.crud import user_crud
from app.models import User
from app.schemas import UserShort

router = APIRouter()


# Todo : Только Руководитель, видит список своих сотрудников
@router.get(
    '/employees',
    response_model=list[UserShort],
    response_model_exclude={'is_active'},
)
async def get_employees(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(only_chief_accesses),
):
    data = await user_crud.get_employees(session=session, user_id=user.id)
    return data
