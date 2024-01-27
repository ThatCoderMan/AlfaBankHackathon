from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud import direction_crud, grade_crud, user_crud
from app.schemas import DirectionRead, GradeRead, UserInfo

router = APIRouter()


@router.get(
    '/direction',
    response_model=list[DirectionRead],
)
async def get_directions(
    session: AsyncSession = Depends(get_async_session),
):
    directions = await direction_crud.get_multi(session=session)
    return directions


@router.get(
    '/grade',
    response_model=list[GradeRead],
)
async def get_grades(
    session: AsyncSession = Depends(get_async_session),
):
    grades = await grade_crud.get_multi(session=session)
    return grades


@router.get('/creators', response_model=list[UserInfo])
async def get_creators(session: AsyncSession = Depends(get_async_session)):
    users = await user_crud.get_templates_creators(session=session)
    return users
