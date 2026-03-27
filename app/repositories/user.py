from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

class UserRepository:
    """Repository for User database operations"""

    @staticmethod
    def get_user_by_id(db: Session, user_id: int):
        """Get user by ID"""
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_user_by_username(db: Session, username: str):
        """Get user by username"""
        return db.query(User).filter(User.username == username).first()

    @staticmethod
    def get_user_by_email(db: Session, email: str):
        """Get user by email"""
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def create_user(db: Session, user: UserCreate, hashed_password: str):
        """Create a new user"""
        db_user = User(
            username=user.username,
            email=user.email,
            full_name=user.full_name,
            hashed_password=hashed_password
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def get_all_users(db: Session, skip: int = 0, limit: int = 10):
        """Get all users with pagination"""
        return db.query(User).offset(skip).limit(limit).all()

    @staticmethod
    def delete_user(db: Session, user_id: int):
        """Delete user by ID"""
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            db.delete(user)
            db.commit()
        return user
