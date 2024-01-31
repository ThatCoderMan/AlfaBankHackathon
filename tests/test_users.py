from app.models import User


async def test_example(fixture_users):
    assert fixture_users == User
