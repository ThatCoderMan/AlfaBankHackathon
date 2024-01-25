from fastapi_users.schemas import BaseUser, BaseUserCreate
from pydantic import BaseModel

from app.models.user import UserRole

from .pdp import PDPShort


class UserRead(BaseUser[int]):
    first_name: str
    last_name: str
    patronymic_name: str | None = None
    position: str
    role: UserRole
    photo: str | None = None


class UserShort(BaseModel):
    id: int
    first_name: str
    last_name: str
    patronymic_name: str | None = None
    position: str
    role: UserRole
    photo: str | None = None
    pdp: PDPShort


class UserInfo(BaseModel):
    id: int
    first_name: str
    last_name: str
    patronymic_name: str | None = None
    position: str
    role: UserRole
    photo: str | None = None


class UserCreate(BaseUserCreate):
    first_name: str
    last_name: str
    patronymic_name: str | None = None
    position: str
    role: UserRole
    photo: str | None = None


class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    patronymic_name: str | None = None
    photo: str | None = None
