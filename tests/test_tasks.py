from app.models import Task


async def test_example(fixture_task):
    assert fixture_task == Task
