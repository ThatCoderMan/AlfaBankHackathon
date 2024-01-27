from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user
from app.crud.template import template_crud
from app.models import User
from app.schemas import TemplateCreate, TemplateRead, TemplateUpdate

router = APIRouter()


@router.get('/{template_id}', response_model=TemplateRead)
async def get_template(
    template_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return await template_crud.get(template_id=template_id, session=session)


@router.post('/', response_model=TemplateRead)
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
)
async def change_template(
    template_id: int,
    template_in: TemplateUpdate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    template_db = await template_crud.get(
        template_id=template_id, session=session
    )
    return await template_crud.update(
        session=session, obj_in=template_in, db_obj=template_db
    )


@router.delete('/{template_id}', status_code=204, deprecated=True)
async def delete_template(
    template_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    template_obj = await template_crud.get(
        template_id=template_id, session=session
    )
    await template_crud.remove(db_obj=template_obj, session=session)
    return {'message': 'ok'}