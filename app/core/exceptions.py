from fastapi import HTTPException, status


class UserAlreadyExistsException(HTTPException):
    """User already exists exception"""

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this username or email already exists",
        )


class UserNotFoundException(HTTPException):
    """User not found exception"""

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )


class InvalidCredentialsException(HTTPException):
    """Invalid credentials exception"""

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )


class ValidationException(HTTPException):
    """Validation error exception"""

    def __init__(self, detail: str = "Validation error"):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail
        )


class NotFoundException(HTTPException):
    """Resource not found exception"""

    def __init__(self, detail: str = "Resource not found"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND, detail=detail
        )


class UnauthorizedException(HTTPException):
    """Unauthorized access exception"""

    def __init__(self, detail: str = "Unauthorized"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=detail
        )


class ForbiddenException(HTTPException):
    """Forbidden access exception"""

    def __init__(self, detail: str = "Forbidden"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN, detail=detail
        )


class ConflictException(HTTPException):
    """Conflict exception (e.g., duplicate resource)"""

    def __init__(self, detail: str = "Conflict"):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT, detail=detail
        )


class BadRequestException(HTTPException):
    """Bad request exception"""

    def __init__(self, detail: str = "Bad request"):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST, detail=detail
        )
