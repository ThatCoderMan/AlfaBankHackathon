from pydantic import BaseModel

from .task_properties import TypeRead
from .template_properties import DirectionRead, GradeRead
from .user import UserInfo


class TemplateBase(BaseModel):
    title: str


class TemplateRead(TemplateBase):
    id: int
    description: str
    skills: list[str] | None
    user: UserInfo
    direction: DirectionRead
    grade: GradeRead
    type: TypeRead
    duration: int | None
    recommendation: str | None

    class Meta:
        orm_mode = True


class TemplateShort(TemplateBase):
    id: int
    user: UserInfo
    direction: DirectionRead
    grade: GradeRead
    type: TypeRead

    class Meta:
        orm_mode = True


class TemplateCreate(TemplateBase):
    description: str
    skills: str
    direction_id: int = 1
    grade_id: int = 1
    type_id: int = 1
    duration: int | None
    recommendation: str | None


class TemplateUpdate(TemplateBase):
    title: str | None = None
    description: str | None = None
    skills: list[str] | None = None
    direction_id: int | None = None
    grade_id: int | None = None
    type_id: int | None = None
    duration: int | None = None
    recommendation: str | None = None
