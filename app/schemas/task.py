from datetime import date

from pydantic import BaseModel, Field, PositiveInt

from core.constants import LENGTH_LIMITS_STRING_FIELDS
from .task_properties import StatusRead, TypeRead


class TaskBase(BaseModel):
    pdp_id: PositiveInt
    starting_date: date
    deadline: date


class TaskRead(TaskBase):
    id: PositiveInt
    type: TypeRead
    status: StatusRead
    description: str | None
    skills: str | None
    chief_comment: str | None
    employee_comment: str | None

    class Meta:
        orm_mode = True


class TaskShort(TaskBase):
    id: PositiveInt
    type: TypeRead
    status: StatusRead

    class Meta:
        orm_mode = True


class TaskCreate(TaskBase):
    type_id: PositiveInt = 1
    status_id: PositiveInt = 1
    description: str
    skills: str = Field(None, max_length=LENGTH_LIMITS_STRING_FIELDS)
    chief_comment: str | None = None
    employee_comment: str | None = None
    starting_date: date = Field(None, min_value=date.today())
    deadline: date = Field(None, min_value=date.today())


class TaskUpdate(TaskBase):
    type_id: PositiveInt | None = None
    status_id: PositiveInt | None = None
    description: str | None = None
    skills: str = Field(None, max_length=LENGTH_LIMITS_STRING_FIELDS)
    chief_comment: str | None = None
    employee_comment: str | None = None
    starting_date: date = Field(None, min_value=date.today())
    deadline: date = Field(None, min_value=date.today())
