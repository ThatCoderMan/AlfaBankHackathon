from pydantic import BaseModel


class Task(BaseModel):
    id: int
    pdp_id: int
    type: int
    description: str
    skills: str
    chief_comment: str
    employee_comment: str
    status: int
    starting_date: str
    deadline: str
