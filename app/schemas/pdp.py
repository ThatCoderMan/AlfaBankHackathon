from datetime import date

from pydantic import BaseModel, Field

from .task import TaskShort


class PDPBase(BaseModel):
    goal: str = Field(max_length=100)
    deadline: date = Field(min_value=date.today())


class PDPRead(PDPBase):
    id: int
    user_id: int
    tasks: list[TaskShort]
    done: int
    total: int

    class Meta:
        orm_mode = True


class PDPShort(PDPBase):
    id: int
    done: int
    total: int

    class Meta:
        orm_mode = True


class PDPCreate(PDPBase):
    user_id: int


class PDPUpdate(BaseModel):
    goal: str | None = None
    deadline: date | None
