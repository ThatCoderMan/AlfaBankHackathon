from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class TaskModel(BaseModel):
    task_id: str
    title: str
    description: str
    status: str
    due_date: str


class IDPRequestModel(BaseModel):
    idp_id: str
    status: str
    created_at: str


class IDPRequestCreateModel(BaseModel):
    employee_id: str
    title: str
    description: str
    start_date: str
    end_date: str
    goal: str


tasks_data = [
    {
        "task_id": "task-uuid1234-5678-90ab-cdef-taskuuid12345678",
        "title": "Завершение курса по управлению проектами",
        "description": "Пройти онлайн-курс для повышения компетенций в "
        "области управления проектами",
        "status": "In Progress",
        "due_date": "2024-12-31",
    },
    {
        "task_id": "task-uuid9876-5432-10ba-fedc-taskuuid98765432",
        "title": "Участие в тренинге по лидерским навыкам",
        "description": "Участвовать во внутреннем тренинге компании по "
        "развитию лидерских качеств",
        "status": "Not Started",
        "due_date": "2024-10-20",
    },
]


@router.get(
    "/{idp_id}/tasks",
    response_model=List[TaskModel],
    response_model_exclude_none=True,
)
async def get_tasks_for_idp(idp_id: str):
    """Получить список задач для конкретного ИПР."""
    return {"tasks": tasks_data}


@router.post(
    "/requests",
    response_model=IDPRequestModel,
)
async def create_idp_request(request_data: IDPRequestCreateModel):
    """Создать заявку на ИПР."""
    return {
        "idp_id": "idp-uuid9876-5432-10ba-fedc-idpuuid987654",
        "status": "Pending",
        "created_at": "2023-03-25 10:00:00",
    }
