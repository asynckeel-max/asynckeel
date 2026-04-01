from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from jose import JWTError
from sqlalchemy.orm import Session
from starlette.requests import Request

from app.core.security import decode_token
from app.db.session import SessionLocal
from app.models.user import User
from app.repositories.user import UserRepository

security = HTTPBearer()


def get_db() -> Session:
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_current_user(
    request: Request,
    db: Session = Depends(get_db),
) -> User:
    """Get current authenticated user"""
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = auth_header.split("Bearer ")[1]
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        token_data = decode_token(token)
        if token_data is None:
            raise credentials_exception
        username: str = token_data.username
    except JWTError:
        raise credentials_exception

    user = UserRepository.get_user_by_username(db, username=username)
    if user is None:
        raise credentials_exception

    return user
