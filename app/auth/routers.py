from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.core.db import get_async_session
from app.core.user import create_access_token, pwd_context
from app.crud.user import get_user, create_user
from app.schemas.user import LoginRequest, Token, RegisterUser, LoginUser

auth_router = APIRouter(tags=['Аутентификация'])


@auth_router.post(path='/token', response_model=Token,
                  summary='Получение JWT токена')
async def login_for_access_token(login_request: LoginUser,
                                 db: AsyncSession = Depends(get_async_session)):
    """Аутентификация пользователя, получение JWT-токена."""

    user = await get_user(db, login_request.email)
    if not user or not pwd_context.verify(login_request.hashed_password,
                                          user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Неверный Пароль или Почта',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    access_token = create_access_token(data={'sub': user.email})
    return {
        'email': user.email,
        'access_token': access_token,
        'token_type': 'bearer',
    }


@auth_router.post(path='/user/', response_model=RegisterUser,
                  summary='Регистрация пользователей')
async def register_user(user: LoginRequest,
                        db: AsyncSession = Depends(get_async_session)):
    """Регистрация нового пользователя."""

    db_user = await get_user(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400,
                            detail='Такой Пользователь Существует !')
    return await create_user(db=db,
                             email=user.email,
                             hashed_password=pwd_context.hash(
                                 user.hashed_password),
                             first_name=user.first_name,
                             last_name=user.last_name,
                             patronymic_name=user.patronymic_name
                             )
