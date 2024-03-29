from datetime import date

from pydantic import BaseModel, Field, PositiveInt

from .task_properties import DirectionRead, SkillRead, TypeRead


class TaskBase(BaseModel):
    title: str
    starting_date: date | None
    deadline: date | None


class TaskRead(TaskBase):
    id: PositiveInt
    pdp_id: PositiveInt
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
    id: PositiveInt
    pdp_id: PositiveInt
    type: TypeRead
    status: DirectionRead

    class Meta:
        orm_mode = True


class TaskCreate(TaskBase):
    type_id: PositiveInt = None
    pdp_id: PositiveInt = None
    status_id: PositiveInt = None
    description: str
    skills: list[str] | None = None
    link: str | None = None
    chief_comment: str | None = None
    employee_comment: str | None = None
    starting_date: date = Field(None, min_value=date.today())
    deadline: date = Field(None, min_value=date.today())


class TaskUpdate(TaskBase):
    type_id: PositiveInt | None = None
    status_id: PositiveInt | None = None
    title: str | None = None
    description: str | None = None
    skills: list[str] | None = None
    link: str | None = None
    chief_comment: str | None = None
    employee_comment: str | None = None
    starting_date: date = Field(None, min_value=date.today())
    deadline: date = Field(None, min_value=date.today())
