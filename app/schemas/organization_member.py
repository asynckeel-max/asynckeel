from datetime import datetime

from pydantic import BaseModel

from app.models.organization_member import RoleEnum


class OrganizationMemberCreate(BaseModel):
    """Create organization member schema"""

    user_id: int
    role: RoleEnum = RoleEnum.MEMBER


class OrganizationMemberUpdate(BaseModel):
    """Update organization member schema"""

    role: RoleEnum


class OrganizationMemberResponse(BaseModel):
    """Organization member response schema"""

    id: int
    organization_id: int
    user_id: int
    role: RoleEnum
    joined_at: datetime

    class Config:
        from_attributes = True
