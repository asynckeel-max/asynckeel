from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user, get_db
from app.models.user import User
from app.schemas.organization import (
    OrganizationCreate,
    OrganizationResponse,
    OrganizationUpdate,
)
from app.services.organization import OrganizationService

router = APIRouter(prefix="/organizations", tags=["organizations"])


@router.post(
    "",
    response_model=OrganizationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_organization(
    org_data: OrganizationCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Create a new organization"""
    return OrganizationService.create_organization(
        db, current_user.id, org_data
    )


@router.get("", response_model=list[OrganizationResponse])
def list_user_organizations(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get all organizations for current user"""
    return OrganizationService.get_user_organizations(db, current_user.id)


@router.get("/{org_id}", response_model=OrganizationResponse)
def get_organization(
    org_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get organization by ID"""
    org = OrganizationService.get_organization(db, org_id)
    return org


@router.put("/{org_id}", response_model=OrganizationResponse)
def update_organization(
    org_id: int,
    org_data: OrganizationUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Update organization (owner only)"""
    return OrganizationService.update_organization(
        db, org_id, current_user.id, org_data
    )


@router.delete("/{org_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_organization(
    org_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Delete organization (owner only)"""
    OrganizationService.delete_organization(db, org_id, current_user.id)
