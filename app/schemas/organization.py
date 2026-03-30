from datetime import datetime

from pydantic import BaseModel


class OrganizationCreate(BaseModel):
    """Create organization schema"""

    name: str
    description: str | None = None


class OrganizationUpdate(BaseModel):
    """Update organization schema"""

    name: str | None = None
    description: str | None = None


class OrganizationResponse(BaseModel):
    """Organization response schema"""

    id: int
    name: str
    description: str | None
    owner_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
