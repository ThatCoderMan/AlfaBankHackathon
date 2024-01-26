from fastapi import Depends, HTTPException, status

from app.core.user import current_user
from app.models import User
from app.models.user import UserRole


def only_chief_accesses(user: User = Depends(current_user)):
    if user.role != UserRole.CHIEF:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f'У пользователя {user.email} '
                   f'Недостаточно прав для выполнения действия'
        )
    return current_user
