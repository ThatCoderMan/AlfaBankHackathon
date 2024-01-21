from typing import Union

from pydantic import BaseModel


class PDPBase(BaseModel):
    user_id: int
    goal: str
    deadline: str


class PDPCreate(PDPBase):
    pass


class PDPRead(PDPBase):
    id: int
    starting_date: str


class PDPUpdate(BaseModel):
    goal: Union[str, None] = None
    deadline: Union[str, None] = None
