from pydantic import BaseModel


class StatusRead(BaseModel):
    id: int
    name: str

    class Meta:
        orm_mode = True
