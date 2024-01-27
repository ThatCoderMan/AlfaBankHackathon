from datetime import date

from pydantic import BaseModel

from .task_properties import DirectionRead, SkillRead, TypeRead


class TaskBase(BaseModel):
    title: str
    starting_date: date
    deadline: date


class TaskRead(TaskBase):
    id: int
    type: TypeRead
    status: DirectionRead
    description: str | None
    skills: list[SkillRead] | None
    link: str | None
    chief_comment: str | None
    employee_comment: str | None

    class Meta:
        orm_mode = True


class TaskShort(TaskBase):
    id: int
    type: TypeRead
    status: DirectionRead

    class Meta:
        orm_mode = True


class TaskCreate(TaskBase):
    pdp_id: int
    type_id: int
    status_id: int
    description: str | None
    skills: list[str] | None = None
    link: str | None = None
    chief_comment: str | None = None
    employee_comment: str | None = None


class TaskUpdate(TaskBase):
    type_id: int | None = None
    title: str | None = None
    status_id: int | None = None
    description: str | None = None
    skills: list[str] | None = None
    link: str | None = None
    chief_comment: str | None = None
    employee_comment: str | None = None
    starting_date: date | None = None
    deadline: date | None = None
