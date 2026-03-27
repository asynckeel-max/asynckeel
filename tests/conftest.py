import pytest

@pytest.fixture
async def example_fixture():
    # Setup that runs before the test
    yield 42  # This value is usable in tests
    # Teardown that runs after the test
