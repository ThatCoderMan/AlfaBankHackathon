from httpx import AsyncClient

from tests.conftest import async_client
from tests.constants import exp_types_task, task_data
from tests.services import authorize_user, compare_type


async def test_create_and_get_task(async_client: AsyncClient,
                                   fixture_task):
    token = await authorize_user(async_client, 'chief@email.com', 'password')

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

    assert response.status_code == 200
    assert compare_type(exp_types_task, retrieved_task)
    assert retrieved_task['title'] == task_data['title']
    assert retrieved_task['starting_date'] == task_data['starting_date']
    assert retrieved_task['deadline'] == task_data['deadline']
    assert retrieved_task['type']['id'] == task_data['type_id']
    assert retrieved_task['pdp_id'] == task_data['pdp_id']
    assert retrieved_task['status']['id'] == task_data['status_id']
    assert retrieved_task['description'] == task_data['description']
    assert retrieved_task['skills'][0]['value'] == task_data['skills'][0]
    assert retrieved_task['link'] == task_data['link']
    assert retrieved_task['chief_comment'] == task_data['chief_comment']
    assert retrieved_task['employee_comment'] == task_data['employee_comment']
