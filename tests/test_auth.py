import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.base import Base
from app.schemas.user import UserCreate
from app.services.auth import AuthService
from app.services.user import UserService
from app.core.exceptions import InvalidCredentialsException

TEST_DATABASE_URL = "sqlite:///:memory:"


@pytest.fixture
def test_db():
    """Create test database"""
    engine = create_engine(
        TEST_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    Base.metadata.create_all(bind=engine)
    TestingSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=engine
    )
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def test_user(test_db):
    """Create test user"""
    user_data = UserCreate(
        username="testuser",
        email="test@example.com",
        full_name="Test User",
        password="testpass123",
    )
    return UserService.create_user(test_db, user_data)


def test_login_success(test_db, test_user):
    """Test successful login"""
    result = AuthService.login(test_db, "testuser", "testpass123")
    assert result["access_token"]
    assert result["token_type"] == "bearer"
    assert result["user_id"] == test_user.id
    assert result["username"] == "testuser"


def test_login_wrong_password(test_db, test_user):
    """Test login with wrong password"""
    with pytest.raises(InvalidCredentialsException):
        AuthService.login(test_db, "testuser", "wrongpassword")


def test_login_nonexistent_user(test_db):
    """Test login with nonexistent user"""
    with pytest.raises(InvalidCredentialsException):
        AuthService.login(test_db, "nonexistent", "password123")
