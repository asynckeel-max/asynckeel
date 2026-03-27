import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base
from app.models.user import User
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate

TEST_DATABASE_URL = "sqlite:///:memory:"

@pytest.fixture
def test_db():
    """Create test database"""
    engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()

def test_create_user(test_db):
    """Test creating a user"""
    user_data = UserCreate(
        username="testuser",
        email="test@example.com",
        full_name="Test User",
        password="testpass123"
    )
    user = UserRepository.create_user(test_db, user_data, "hashed_password")
    assert user.username == "testuser"
    assert user.email == "test@example.com"

def test_get_user_by_username(test_db):
    """Test getting user by username"""
    user_data = UserCreate(
        username="testuser",
        email="test@example.com",
        full_name="Test User",
        password="testpass123"
    )
    UserRepository.create_user(test_db, user_data, "hashed_password")
    user = UserRepository.get_user_by_username(test_db, "testuser")
    assert user is not None
    assert user.username == "testuser"
