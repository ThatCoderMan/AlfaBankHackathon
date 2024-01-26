from datetime import date

from pydantic import BaseModel, Field

from core.constants import LENGTH_LIMITS_STRING_FIELDS
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
    type_id: int = 0
    status_id: int
    description: str | None
    skills: str = Field(None, max_length=LENGTH_LIMITS_STRING_FIELDS)
    chief_comment: str | None = None
    employee_comment: str | None = None
    starting_date: date = Field(None, min_value=date.today())
    deadline: date = Field(min_value=date.today())


class TaskUpdate(TaskBase):
    type_id: int | None
    status_id: int | None
    description: str | None
    skills: str = Field(None, max_length=LENGTH_LIMITS_STRING_FIELDS)
    chief_comment: str | None
    employee_comment: str | None
    starting_date: date = Field(None, min_value=date.today())
    deadline: date = Field(None, min_value=date.today())
