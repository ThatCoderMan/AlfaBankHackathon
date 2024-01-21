from typing import Union

from pydantic import BaseModel


class TaskBase(BaseModel):
    type: int
    description: str
    skills: str
    chief_comment: Union[str, None] = None
    employee_comment: Union[str, None] = None
    status: int
    deadline: str


class TaskCreate(TaskBase):
    pass


class TaskRead(TaskBase):
    id: int
    pdp_id: int
    starting_date: str


class TypeUpdate(TaskBase):
    type: Union[int, None] = None
    description: Union[str, None] = None
    skills: Union[str, None] = None
    chief_comment: Union[str, None] = None
    employee_comment: Union[str, None] = None
    status: int
    deadline: Union[str, None] = None
