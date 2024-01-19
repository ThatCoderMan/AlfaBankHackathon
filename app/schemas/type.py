from pydantic import BaseModel


class TypeBase(BaseModel):
    id: int
    name: str
