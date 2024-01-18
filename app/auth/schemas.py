from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    """
    Модель для чтения информации о пользователе.
    """

    first_name: str
    last_name: str
    patronymic_name: str
    email: str


class UserCreate(schemas.BaseUserCreate):
    """
    Модель для чтения информации о пользователе.
    """

    id: int
    first_name: str
    last_name: str
    patronymic_name: str
    email: str
    is_active: bool
    is_superuser: bool
    is_verified: bool
