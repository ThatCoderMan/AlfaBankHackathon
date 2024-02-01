from httpx import AsyncClient

from tests.conftest import async_client
from tests.constants import exp_types_task
from tests.services import authorize_user, compare_type


async def test_create_and_get_task(async_client: AsyncClient,
                                   fixture_task):
    token = await authorize_user(async_client, 'chief@email.com', 'password')

    task_data = {
        'title': "Тест_Title",
        'starting_date': "2024-02-01",
        'deadline': "2025-02-01",
        'type_id': 1,
        'pdp_id': 1,
        'status_id': 1,
        'description': 'Описание Задачи',
        'skills': ['волшебник'],
        'link': 'http://task_link',
        'chief_comment': '',
        'employee_comment': ''
    }

    response = await async_client.post('/api/v1/task/',
                                       headers={
                                           'Authorization': f'Bearer {token}'},
                                       json=task_data)
    assert response.status_code == 200
    created_task = response.json()

    task_id = created_task['id']
    response = await async_client.get(f'/api/v1/task/{task_id}',
                                      headers={
                                          'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    retrieved_task = response.json()

    assert compare_type(exp_types_task, retrieved_task)
    assert retrieved_task['title'] == task_data['title']
    assert retrieved_task['description'] == task_data['description']
