from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user, get_db
from app.models.user import User
from app.schemas.organization_member import (
    OrganizationMemberCreate,
    OrganizationMemberResponse,
    OrganizationMemberUpdate,
)
from app.services.organization_member import OrganizationMemberService

router = APIRouter(
    prefix="/organizations/{org_id}/members",
    tags=["organization-members"],
)


@router.post(
    "",
    response_model=OrganizationMemberResponse,
    status_code=status.HTTP_201_CREATED,
)
def add_member(
    org_id: int,
    member_data: OrganizationMemberCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Add member to organization (admin/owner only)"""
    return OrganizationMemberService.add_member(
        db, org_id, member_data.user_id, current_user.id, member_data.role
    )


@router.get("", response_model=list[OrganizationMemberResponse])
def get_organization_members(
    org_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get all members of organization"""
    return OrganizationMemberService.get_organization_members(db, org_id)


@router.get("/{user_id}", response_model=OrganizationMemberResponse)
def get_member(
    org_id: int,
    user_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get specific member"""
    return OrganizationMemberService.get_member(db, org_id, user_id)


@router.put("/{user_id}", response_model=OrganizationMemberResponse)
def update_member_role(
    org_id: int,
    user_id: int,
    role_data: OrganizationMemberUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Update member role (owner only)"""
    return OrganizationMemberService.update_member_role(
        db, org_id, user_id, current_user.id, role_data
    )


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_member(
    org_id: int,
    user_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Remove member from organization (admin/owner only)"""
    OrganizationMemberService.remove_member(
        db, org_id, user_id, current_user.id
    )
