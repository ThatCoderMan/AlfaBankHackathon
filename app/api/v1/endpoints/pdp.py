from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_chief, current_user
from app.models import User
from app.schemas import PDPRead, PDPUpdate

router = APIRouter()


@router.get(
    '/{pdp_id}',
    response_model=PDPRead,
)
async def get_pdp(
    pdp_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return {None}


@router.patch(
    '/{pdp_id}',
    response_model=PDPRead,
)
async def change_pdp(
    pdp_id: int,
    pdp_obj: PDPUpdate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_chief),
):
    return {None}
