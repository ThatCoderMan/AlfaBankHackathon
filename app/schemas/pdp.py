from pydantic import BaseModel

from .task import TaskShort


class PDPBase(BaseModel):
    goal: str
    deadline: str


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
    deadline: str | None = None
