from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user
from app.crud import skill_crud, status_crud, type_crud
from app.models import User
from app.schemas import DirectionRead, SkillRead, TypeRead

router = APIRouter()


@router.get(
    '/statuses',
    response_model=list[DirectionRead],
)
async def get_status(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    statuses = await status_crud.get_multi_by_role(session=session, user=user)
    return statuses


@router.get(
    '/types',
    response_model=list[TypeRead],
)
async def get_type_of_task(
    session: AsyncSession = Depends(get_async_session),
):
    types = await type_crud.get_multi(session=session)
    return types


@router.get(
    '/skills/',
    response_model=list[SkillRead],
)
async def get_skills(
    q: str = "",
    session: AsyncSession = Depends(get_async_session),
):
    skills = await skill_crud.get_by_query(session=session, query=q)
    return skills
