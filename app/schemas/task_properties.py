from pydantic import BaseModel, PositiveInt


class TypeRead(BaseModel):
    id: PositiveInt
    name: str

    class Meta:
        orm_mode = True


class StatusRead(BaseModel):
    id: PositiveInt
    name: str

    class Meta:
        orm_mode = True
