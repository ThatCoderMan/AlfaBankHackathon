from pydantic import BaseModel


class TypeRead(BaseModel):
    id: int
    value: str

    class Meta:
        orm_mode = True


class DirectionRead(BaseModel):
    id: int
    value: str

    class Meta:
        orm_mode = True


class SkillRead(BaseModel):
    id: int
    value: str

    class Meta:
        orm_mode = True
