from datetime import date

from pydantic import BaseModel, Field, PositiveInt

from app.core.constants import LENGTH_LIMITS_STRING_FIELDS

from .task import TaskShort


class PDPBase(BaseModel):
    goal: str = Field(max_length=LENGTH_LIMITS_STRING_FIELDS)
    starting_date: date
    deadline: date


class PDPRead(PDPBase):
    id: PositiveInt
    user_id: PositiveInt
    tasks: list[TaskShort]
    done: int
    total: int

    class Meta:
        orm_mode = True


class PDPShort(PDPBase):
    id: PositiveInt
    done: int
    total: int

    class Meta:
        orm_mode = True


class PDPCreate(PDPBase):
    user_id: PositiveInt
    starting_date: date = Field(min_value=date.today())
    deadline: date = Field(min_value=date.today())


class PDPUpdate(BaseModel):
    goal: str = Field(None, max_length=LENGTH_LIMITS_STRING_FIELDS)
    starting_date: date = Field(None, min_value=date.today())
    deadline: date = Field(None, min_value=date.today())
