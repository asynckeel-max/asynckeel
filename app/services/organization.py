from sqlalchemy.orm import Session

from app.core.exceptions import (
    NotFoundException,
    UnauthorizedException,
)
from app.models.organization_member import RoleEnum
from app.repositories.organization import OrganizationRepository
from app.repositories.organization_member import (
    OrganizationMemberRepository,
)
from app.schemas.organization import (
    OrganizationCreate,
    OrganizationUpdate,
)


class OrganizationService:
    """Service for organization operations"""

    @staticmethod
    def create_organization(
        db: Session, user_id: int, org_data: OrganizationCreate
    ):
        """Create a new organization and add user as owner"""
        # Create organization
        org = OrganizationRepository.create_organization(
            db, org_data.name, org_data.description, user_id
        )

        # Add creator as owner member
        OrganizationMemberRepository.add_member(
            db, org.id, user_id, RoleEnum.OWNER
        )

        return org

    @staticmethod
    def get_organization(db: Session, org_id: int):
        """Get organization by ID"""
        org = OrganizationRepository.get_organization_by_id(db, org_id)
        if not org:
            raise NotFoundException("Organization not found")
        return org

    @staticmethod
    def get_user_organizations(db: Session, user_id: int):
        """Get all organizations where user is member"""
        memberships = (
            OrganizationMemberRepository.get_user_organizations(
                db, user_id
            )
        )
        return [m.organization for m in memberships]

    @staticmethod
    def update_organization(
        db: Session, org_id: int, user_id: int, org_data: OrganizationUpdate
    ):
        """Update organization (only owner can update)"""
        org = OrganizationService.get_organization(db, org_id)

        # Check if user is owner
        member = OrganizationMemberRepository.get_member(
            db, org_id, user_id
        )
        if not member or member.role != RoleEnum.OWNER:
            raise UnauthorizedException(
                "Only owner can update organization"
            )

        # Update organization
        updated_org = OrganizationRepository.update_organization(
            db,
            org_id,
            org_data.name,
            org_data.description,
        )
        return updated_org

    @staticmethod
    def delete_organization(db: Session, org_id: int, user_id: int):
        """Delete organization (only owner can delete)"""
        org = OrganizationService.get_organization(db, org_id)

        # Check if user is owner
        member = OrganizationMemberRepository.get_member(
            db, org_id, user_id
        )
        if not member or member.role != RoleEnum.OWNER:
            raise UnauthorizedException(
                "Only owner can delete organization"
            )

        # Delete organization
        return OrganizationRepository.delete_organization(db, org_id)
