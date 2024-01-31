from app.models import Grade


async def test_example(fixture_grade):
    assert fixture_grade == Grade
