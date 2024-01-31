from app.models import Skill


async def test_example(fixture_skill):
    assert fixture_skill == Skill
