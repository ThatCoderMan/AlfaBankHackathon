from pydantic import BaseModel


class DirectionRead(BaseModel):
    id: int
    value: str

    class Meta:
        orm_mode = True


class GradeRead(BaseModel):
    id: int
    value: str

    class Meta:
        orm_mode = True
