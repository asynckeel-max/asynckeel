from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.exceptions import InvalidCredentialsException
from app.db.session import get_db
from app.schemas.auth import LoginRequest, LoginResponse
from app.services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/login", response_model=LoginResponse, status_code=status.HTTP_200_OK
)
def login(credentials: LoginRequest, db: Session = Depends(get_db)):
    """Login with username and password"""
    try:
        return AuthService.login(
            db, credentials.username, credentials.password
        )
    except InvalidCredentialsException as e:
        raise e
