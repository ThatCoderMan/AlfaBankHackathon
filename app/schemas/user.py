from pydantic import EmailStr, BaseModel


class LoginUser(BaseModel):
    """
    Модель для аутентификации пользователя.
    """

    email: EmailStr
    hashed_password: str


class Token(BaseModel):
    """
    Модель для выдачи токена.
    """

    email: EmailStr
    access_token: str
    token_type: str


class LoginRequest(BaseModel):
    """
    Модель для запроса при регистрации пользователя.
    """

    first_name: str
    last_name: str
    patronymic_name: str
    email: EmailStr
    hashed_password: str


class RegisterUser(BaseModel):
    """
    Модель для ответа при регистрации пользователя.
    """

    first_name: str
    last_name: str
    patronymic_name: str
    email: EmailStr
