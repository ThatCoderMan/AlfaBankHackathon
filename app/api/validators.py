from fastapi import HTTPException, status, Depends
from sqlalchemy import select

from app.models import PDP, Type, Status
from app.core.user import current_user
from app.models import User
from app.models.user import UserRole


async def get_or_404(obj, session):
    obj_dict = obj.dict()
    obj_id = {
        PDP: obj_dict.get('pdp_id'),
        Type: obj_dict.get('type_id'),
        Status: obj_dict.get('status_id')
    }

    for model, id_model in obj_id.items():
        res = await session.execute(
            select(model).where(model.id == id_model)
        )
        if res.scalars().first() is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return obj


def only_chief(user: User = Depends(current_user)):
    if user.role != UserRole.CHIEF:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Недостаточно прав для выполнения действия',
        )
    return current_user
