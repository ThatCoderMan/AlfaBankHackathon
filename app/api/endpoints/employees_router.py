from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class EmployeeModel(BaseModel):
    employee_id: str
    name: str
    position: str


employees_data = [
    {
        "employee_id": "uuid1234-5678-90ab-cdef-uuid12345678",
        "name": "Иван " "Иванов",
        "position": "Менеджер проекта",
    },
    {
        "employee_id": "uuid8765-4321-ba09-fedc-uuid87654321",
        "name": "Мария " "Петрова",
        "position": "Аналитик",
    },
]


@router.get(
    "/",
    response_model=List[EmployeeModel],
    response_model_exclude_none=True,
)
async def get_all_employees():
    """Получить список всех сотрудников."""
    return employees_data
