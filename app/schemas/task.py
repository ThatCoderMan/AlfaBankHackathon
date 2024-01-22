from datetime import date

from pydantic import BaseModel

from .task_properties import StatusRead, TypeRead


class TaskBase(BaseModel):
    type: TypeRead
    status: StatusRead
    starting_date: date
    deadline: date


class TaskRead(TaskBase):
    id: int
    description: str | None
    skills: str | None
    chief_comment: str | None
    employee_comment: str | None

    class Meta:
        orm_mode = True


class TaskShort(TaskBase):
    id: int

    class Meta:
        orm_mode = True


class TaskCreate(TaskBase):
    type: int
    status: int
    description: str | None
    skills: str | None
    chief_comment: str | None = None
    employee_comment: str | None = None


class TaskUpdate(TaskBase):
    type: int | None
    status: int | None
    description: str | None
    skills: str | None
    chief_comment: str | None
    employee_comment: str | None
    starting_date: date | None
    deadline: date | None
