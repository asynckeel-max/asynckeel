from sqlalchemy.orm import Session

from app.core.exceptions import (
    NotFoundException,
    UnauthorizedException,
)
from app.models.organization_member import RoleEnum
from app.repositories.organization_member import (
    OrganizationMemberRepository,
)
from app.repositories.user import UserRepository
from app.schemas.organization_member import OrganizationMemberUpdate


class OrganizationMemberService:
    """Service for organization member operations"""

    @staticmethod
    def add_member(
        db: Session, org_id: int, user_id: int, requester_id: int,
        role: RoleEnum = RoleEnum.MEMBER
    ):
        """Add member to organization (only admin/owner can add)"""
        # Check if requester is admin or owner
        requester = OrganizationMemberRepository.get_member(
            db, org_id, requester_id
        )
        if not requester or requester.role not in [
            RoleEnum.OWNER,
            RoleEnum.ADMIN,
        ]:
            raise UnauthorizedException(
                "Only owner or admin can add members"
            )

        # Check if user exists
        user = UserRepository.get_user_by_id(db, user_id)
        if not user:
            raise NotFoundException("User not found")

        # Check if user already member
        existing = OrganizationMemberRepository.get_member(
            db, org_id, user_id
        )
        if existing:
            raise ValueError("User is already a member")

        # Add member
        return OrganizationMemberRepository.add_member(
            db, org_id, user_id, role
        )

    @staticmethod
    def remove_member(
        db: Session, org_id: int, user_id: int, requester_id: int
    ):
        """Remove member from organization"""
        # Check if requester is admin or owner
        requester = OrganizationMemberRepository.get_member(
            db, org_id, requester_id
        )
        if not requester or requester.role not in [
            RoleEnum.OWNER,
            RoleEnum.ADMIN,
        ]:
            raise UnauthorizedException(
                "Only owner or admin can remove members"
            )

        # Cannot remove owner
        member = OrganizationMemberRepository.get_member(
            db, org_id, user_id
        )
        if member and member.role == RoleEnum.OWNER:
            raise ValueError("Cannot remove organization owner")

        # Remove member
        return OrganizationMemberRepository.remove_member(
            db, org_id, user_id
        )

    @staticmethod
    def update_member_role(
        db: Session, org_id: int, user_id: int, requester_id: int,
        role_data: OrganizationMemberUpdate
    ):
        """Update member role"""
        # Check if requester is owner
        requester = OrganizationMemberRepository.get_member(
            db, org_id, requester_id
        )
        if not requester or requester.role != RoleEnum.OWNER:
            raise UnauthorizedException(
                "Only owner can change member roles"
            )

        # Check member exists
        member = OrganizationMemberRepository.get_member(
            db, org_id, user_id
        )
        if not member:
            raise NotFoundException("Member not found")

        # Cannot change owner role
        if member.role == RoleEnum.OWNER:
            raise ValueError("Cannot change owner role")

        # Update role
        return OrganizationMemberRepository.update_member_role(
            db, org_id, user_id, role_data.role
        )

    @staticmethod
    def get_organization_members(db: Session, org_id: int):
        """Get all members of organization"""
        return OrganizationMemberRepository.get_organization_members(
            db, org_id
        )

    @staticmethod
    def get_member(db: Session, org_id: int, user_id: int):
        """Get specific member"""
        member = OrganizationMemberRepository.get_member(
            db, org_id, user_id
        )
        if not member:
            raise NotFoundException("Member not found")
        return member
