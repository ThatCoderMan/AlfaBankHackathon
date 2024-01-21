from pydantic import BaseModel


class PDPBase(BaseModel):
    id: int
    user_id: int
    goal: str
    starting_date: str
    deadline: str
