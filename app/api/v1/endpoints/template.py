from pydantic import PositiveInt

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.permissions import only_chief_accesses
from app.core import exceptions
from app.core.db import get_async_session
from app.core.user import current_user
from app.crud.template import template_crud
from app.models import User, Template
from app.schemas import (
    TaskFromTemplateCreate,
    TemplateCreate,
    TemplateFromTaskCreate,
    TemplateRead,
    TemplateUpdate,
)
from app.services import create_tasks_from_template, create_template_from_task

router = APIRouter()


@router.get('/', response_model=list[TemplateRead])
async def get_templates(
        q: str | None = None,
        direction: PositiveInt | None = None,
        skills: list[PositiveInt] = Query(None),
        grade: list[PositiveInt] = Query(None),
        type: PositiveInt | None = None,
        duration_from: PositiveInt | None = None,
        duration_to: PositiveInt | None = None,
        creator: PositiveInt | None = None,
        session: AsyncSession = Depends(get_async_session),
):
    return await template_crud.get_multi(
        session=session,
        q=q,
        direction=direction,
        skills=skills,
        grade=grade,
        type=type,
        duration_from=duration_from,
        duration_to=duration_to,
        creator=creator,
    )


@router.get('/{template_id}', response_model=TemplateRead)
async def get_template(
        template_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    template_obj = await template_crud.get(
        template_id=template_id,
        session=session
    )
    if template_obj is None:
        raise exceptions.NotExistException(model=Template, pk=template_id)
    return template_obj


@router.post(
    '/',
    response_model=TemplateRead,
    dependencies=[Depends(only_chief_accesses)]
)
async def create_template(
        template_in: TemplateCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    template_obj = await template_crud.create(
        session=session, obj_in=template_in, user_id=user.id
    )
    return await template_crud.get(
        session=session, template_id=template_obj.id
    )


@router.patch(
    '/{template_id}',
    response_model=TemplateRead,
    dependencies=[Depends(only_chief_accesses)]
)
async def change_template(
        template_id: int,
        template_in: TemplateUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    template_db = await template_crud.get(
        template_id=template_id, session=session
    )
    if template_db is None:
        raise exceptions.NotExistException(model=Template, pk=template_id)
    return await template_crud.update(
        session=session, obj_in=template_in, db_obj=template_db
    )


@router.delete(
    '/{template_id}',
    status_code=204,
    deprecated=True,
    dependencies=[Depends(only_chief_accesses)]
)
async def delete_template(
        template_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    template_obj = await template_crud.get(
        template_id=template_id, session=session
    )
    if template_obj is None:
        raise exceptions.NotExistException(model=Template, pk=template_id)
    await template_crud.remove(db_obj=template_obj, session=session)
    return {'details': 'ok'}


@router.post(
    '/set_users',
    status_code=201,
    dependencies=[Depends(only_chief_accesses)]
)
async def set_template_to_users(
        data: TaskFromTemplateCreate,
        session: AsyncSession = Depends(get_async_session),
):
    await create_tasks_from_template(
        session=session,
        template_id=data.template_id,
        users_ids=set(data.users_ids),
    )


@router.post(
    '/create_from_task',
    status_code=201,
    dependencies=[Depends(only_chief_accesses)]
)
async def create_from_task(
        data: TemplateFromTaskCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    await create_template_from_task(
        session=session, task_id=data.task_id, user=user
    )
