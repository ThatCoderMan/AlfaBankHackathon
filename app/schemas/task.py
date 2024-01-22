from datetime import date
from pydantic import BaseModel


class TaskBase(BaseModel):
    type: int
    description: str
    skills: str
    chief_comment: str | None = None
    employee_comment: str | None = None
    status: int
    starting_date: date
    deadline: date


class TaskCreate(TaskBase):
    pass


class TaskRead(TaskBase):
    id: int
    pdp_id: int
    starting_date: date

    class Meta:
        orm_mode = True


class TypeUpdate(TaskBase):
    type: int | None
    description: str | None
    skills: str | None
    chief_comment: str | None
    employee_comment: str | None
    status: int
    starting_date: date
    deadline: date | None
