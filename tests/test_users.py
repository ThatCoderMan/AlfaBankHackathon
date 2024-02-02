from app.models import User
from app.models.user import user_user


async def test_example(fixture_users, fixture_user_user):
    assert fixture_users == User
    assert fixture_user_user == user_user
