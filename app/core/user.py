from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext

from app.core.config import Settings

SECRET = Settings().secret

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: dict):
    """
    Создает JWT-токен для предоставленных данных.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=360000)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET)
    return encoded_jwt
