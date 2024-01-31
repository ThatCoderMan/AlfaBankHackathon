from app.models import Type


async def test_example(fixture_type):
    assert fixture_type == Type
