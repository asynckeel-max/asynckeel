from sqlalchemy.orm import Session

from app.core.exceptions import InvalidCredentialsException
from app.core.security import (
    create_access_token,
    verify_password,
)
from app.repositories.user import UserRepository


class AuthService:
    """Service for authentication"""

    @staticmethod
    def authenticate_user(db: Session, username: str, password: str):
        """Authenticate user and return user object"""
        user = UserRepository.get_user_by_username(db, username)
        if not user:
            raise InvalidCredentialsException()

        if not verify_password(password, user.hashed_password):
            raise InvalidCredentialsException()

        return user

    @staticmethod
    def login(db: Session, username: str, password: str):
        """Login user and return access token"""
        user = AuthService.authenticate_user(db, username, password)
        access_token = create_access_token(data={"sub": user.username})
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user_id": user.id,
            "username": user.username,
        }
