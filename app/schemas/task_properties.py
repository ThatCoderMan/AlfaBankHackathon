from pydantic import BaseModel, PositiveInt


class TypeRead(BaseModel):
    id: PositiveInt
    value: str

    class Meta:
        orm_mode = True


class DirectionRead(BaseModel):
    id: PositiveInt
    value: str

    class Meta:
        orm_mode = True


class SkillRead(BaseModel):
    id: PositiveInt
    value: str

    class Meta:
        orm_mode = True
