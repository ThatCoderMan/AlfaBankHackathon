from fastapi_users import schemas
from pydantic import EmailStr


class UserRead(schemas.BaseUser[int]):
    """
    Модель для чтения информации о пользователе.
    """

    first_name: str
    last_name: str
    patronymic_name: str
    email: EmailStr


class UserCreate(schemas.BaseUserCreate):
    """
    Модель для Создания пользователя.
    """

    id: int
    first_name: str
    last_name: str
    patronymic_name: str
    email: EmailStr
    password: str
