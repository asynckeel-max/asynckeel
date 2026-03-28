import pytest
import sys
from pathlib import Path

# Add the project root to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

@pytest.fixture
def example_fixture():
    """Example fixture for testing"""
    yield 42