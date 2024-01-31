from pydantic import BaseModel, PositiveInt


class DirectionRead(BaseModel):
    id: PositiveInt
    value: str

    class Meta:
        orm_mode = True


class GradeRead(BaseModel):
    id: PositiveInt
    value: str

    class Meta:
        orm_mode = True
