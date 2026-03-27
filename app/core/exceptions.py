from fastapi import HTTPException, status

class UserAlreadyExistsException(HTTPException):
    """User already exists exception"""
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this username or email already exists"
        )

class UserNotFoundException(HTTPException):
    """User not found exception"""
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

class InvalidCredentialsException(HTTPException):
    """Invalid credentials exception"""
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

class ValidationException(HTTPException):
    """Validation error exception"""
    def __init__(self, detail: str = "Validation error"):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=detail
        )
