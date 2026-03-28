from sqlalchemy.orm import Session

from app.core.exceptions import UserAlreadyExistsException, UserNotFoundException
from app.core.security import hash_password
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate


class UserService:
    """Service for user business logic"""

    @staticmethod
    def create_user(db: Session, user: UserCreate):
        """Create a new user with validation"""
        # Check if user already exists
        existing_user = UserRepository.get_user_by_username(db, user.username)
        if existing_user:
            raise UserAlreadyExistsException()

        existing_email = UserRepository.get_user_by_email(db, user.email)
        if existing_email:
            raise UserAlreadyExistsException()

        # Hash password and create user
        hashed_password = hash_password(user.password)
        return UserRepository.create_user(db, user, hashed_password)

    @staticmethod
    def get_user(db: Session, user_id: int):
        """Get user by ID"""
        user = UserRepository.get_user_by_id(db, user_id)
        if not user:
            raise UserNotFoundException()
        return user

    @staticmethod
    def get_all_users(db: Session, skip: int = 0, limit: int = 10):
        """Get all users"""
        return UserRepository.get_all_users(db, skip, limit)

    @staticmethod
    def delete_user(db: Session, user_id: int):
        """Delete user"""
        user = UserRepository.delete_user(db, user_id)
        if not user:
            raise UserNotFoundException()
        return user
