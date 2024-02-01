from httpx import AsyncClient
from sqlalchemy import select

from app.models import Direction
from tests import constants
from tests.conftest import async_session_marker, async_client
from tests.constants import exp_types_common
from tests.services import data_to_dict, compare_type


async def test_directions(fixture_directions: Direction,
                          async_client: AsyncClient):
    async with async_session_marker() as session:
        query = select(fixture_directions)
        res = await session.execute(query)
        directions_obj = res.scalars().all()

        result = await data_to_dict(directions_obj)

        exp_type = await compare_type(result, exp_types_common)

        endpoint_url = "/api/v1/template_properties/direction/"
        response = await async_client.get(endpoint_url)

        assert exp_type
        assert result is not None
        assert len(result) == len(constants.directions)
        assert response.status_code == 307
