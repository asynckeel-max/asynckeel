from datetime import datetime

from pydantic import BaseModel


class ApiKeyCreate(BaseModel):
    """Create API key schema"""

    name: str


class ApiKeyResponse(BaseModel):
    """API key response schema (without hash)"""

    id: int
    organization_id: int
    name: str
    is_active: bool
    created_at: datetime
    last_used_at: datetime | None
    expires_at: datetime | None

    class Config:
        from_attributes = True


class ApiKeyCreateResponse(BaseModel):
    """API key creation response (with plain key)"""

    id: int
    organization_id: int
    name: str
    key: str  # Only shown once during creation
    created_at: datetime

    class Config:
        from_attributes = True
