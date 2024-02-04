from pydantic import BaseModel, PositiveInt

from .task_properties import SkillRead, TypeRead
from .template_properties import DirectionRead, GradeRead
from .user import UserInfo


class TemplateBase(BaseModel):
    title: str


class TemplateRead(TemplateBase):
    id: PositiveInt
    description: str
    skills: list[SkillRead] | None
    user: UserInfo
    direction: DirectionRead
    grade: GradeRead
    type: TypeRead
    link: str | None
    duration: PositiveInt | None
    recommendation: str | None

    class Meta:
        orm_mode = True


class TemplateShort(TemplateBase):
    id: PositiveInt
    user: UserInfo
    direction: DirectionRead
    grade: GradeRead
    type: TypeRead

    class Meta:
        orm_mode = True


class TemplateCreate(TemplateBase):
    description: str
    skills: set[str]
    direction_id: PositiveInt = 1
    grade_id: PositiveInt = 1
    type_id: PositiveInt = 1
    link: str | None = None
    duration: PositiveInt | None = None
    recommendation: str | None = None


class TemplateUpdate(TemplateBase):
    title: str | None = None
    description: str | None = None
    skills: set[str] | None = None
    direction_id: PositiveInt | None = None
    grade_id: PositiveInt | None = None
    type_id: PositiveInt | None = None
    link: str | None = None
    duration: PositiveInt | None = None
    recommendation: str | None = None


class TaskFromTemplateCreate(BaseModel):
    users_ids: list[int]
    template_id: PositiveInt


class TemplateFromTaskCreate(BaseModel):
    task_id: PositiveInt
