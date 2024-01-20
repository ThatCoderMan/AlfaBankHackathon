from pydantic import BaseModel


class StatusBase(BaseModel):
    id: int
    name: str
    role: str
