from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user
from app.models import User
from app.schemas import UserRead

router = APIRouter()


@router.get(
    '/employees',
    response_model=list[UserRead],
)
async def get_employees(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return {None}
