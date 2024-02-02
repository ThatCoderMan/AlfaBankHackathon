from httpx import AsyncClient

from tests.conftest import async_client
from tests.constants import exp_types_task, task_data
from tests.services import authorize_user, compare_type_task


async def test_chief_post_get_task(async_client: AsyncClient,
                                   fixture_task):
    token = await authorize_user(async_client, 'chief@email.com', 'password')

    response = await async_client.post('/api/v1/task/',
                                       headers={
                                           'Authorization': f'Bearer {token}'},
                                       json=task_data)
    assert response.status_code == 403

    task_data.pop('employee_comment', None)
    task_data['type_id'] = 999
    response = await async_client.post('/api/v1/task/',
                                       headers={
                                           'Authorization': f'Bearer {token}'},
                                       json=task_data)

    assert response.status_code == 404

    task_data['type_id'] = 1
    task_data['pdp_id'] = 99
    response = await async_client.post('/api/v1/task/',
                                       headers={
                                           'Authorization': f'Bearer {token}'},
                                       json=task_data)

    assert response.status_code == 404

    task_data['pdp_id'] = 1
    response = await async_client.post('/api/v1/task/',
                                       headers={
                                           'Authorization': f'Bearer {token}'},
                                       json=task_data)

    retrieved_task = response.json()
    exp_tp = await compare_type_task(retrieved_task, exp_types_task)

    assert response.status_code == 200
    assert exp_tp
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

    created_task = response.json()

    task_id = created_task['id']

    response = await async_client.get(f'/api/v1/task/{task_id}',
                                      headers={
                                          'Authorization': f'Bearer {token}'})
    assert response.status_code == 403

    response = await async_client.get(f'/api/v1/task/{4}',
                                      headers={
                                          'Authorization': f'Bearer {token}'})
    print(response)
    assert response.status_code == 200
