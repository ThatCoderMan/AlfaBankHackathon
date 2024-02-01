from httpx import AsyncClient


async def authorize_user(async_client: AsyncClient, email: str,
                         password: str) -> str:
    """
    Передаем email Руководителя chief@email.com
    или Сотрудника employee@email.com, и вторым аргументом password,
    и получаем соответствующую роль и юзера.
    """
    user_data = {'username': email, 'password': password}
    response = await async_client.post('/auth/jwt/login', data=user_data)

    assert response.status_code == 200
    return response.json()['access_token']


async def data_to_dict(obj):
    """Преобразование объектов в список словарей."""

    result = [
        {c.name: getattr(md, c.name) for c in md.__table__.columns} for md
        in obj]
    return result


async def compare_type(must, expected):
    """Проверка на тип данных"""

    for key, expected_type in expected.items():
        assert isinstance(must[0][key],
                          expected_type), f"Неверный тип данных для {key}"
    return True
