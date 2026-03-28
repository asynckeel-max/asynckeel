import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Test Database Configuration
TEST_DATABASE_URL = "sqlite:///./test.db"


@pytest.fixture
def test_db():
    """Fixture for test database"""
    engine = create_engine(TEST_DATABASE_URL)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return TestingSessionLocal()


def test_database_connection(test_db):
    """Test database connection"""
    assert test_db is not None


def test_session_is_active(test_db):
    """Test that session is active"""
    assert test_db.is_active
