from app.models import Direction


async def test_example(fixture_directions):
    assert fixture_directions == Direction
