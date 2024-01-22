from pydantic import BaseModel


class TypeRead(BaseModel):
    id: int
    name: str

    class Meta:
        orm_mode = True
