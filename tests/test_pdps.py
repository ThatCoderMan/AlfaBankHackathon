from app.models import PDP


async def test_example(fixture_pdp):
    assert fixture_pdp == PDP
