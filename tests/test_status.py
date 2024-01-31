from app.models import Status


async def test_example(fixture_status):
    assert fixture_status == Status
