from pydantic import BaseModel


class TypeRead(BaseModel):
    id: int
    name: str
