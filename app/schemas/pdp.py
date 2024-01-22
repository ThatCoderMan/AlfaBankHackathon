from pydantic import BaseModel


class PDPBase(BaseModel):
    user_id: int
    goal: str
    deadline: str


class PDPCreate(PDPBase):
    pass


class PDPRead(PDPBase):
    id: int
    starting_date: str

    class Meta:
        orm_mode = True


class PDPUpdate(BaseModel):
    goal: str | None = None
    deadline: str | None = None
