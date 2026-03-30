from sqlalchemy.orm import Session

from app.models.organization_member import (
    OrganizationMember,
    RoleEnum,
)


class OrganizationMemberRepository:
    """Repository for organization member operations"""

    @staticmethod
    def add_member(
        db: Session,
        organization_id: int,
        user_id: int,
        role: RoleEnum = RoleEnum.MEMBER,
    ) -> OrganizationMember:
        """Add a member to organization"""
        member = OrganizationMember(
            organization_id=organization_id, user_id=user_id, role=role
        )
        db.add(member)
        db.commit()
        db.refresh(member)
        return member

    @staticmethod
    def get_member(
        db: Session, organization_id: int, user_id: int
    ) -> OrganizationMember | None:
        """Get organization member"""
        return (
            db.query(OrganizationMember)
            .filter(
                OrganizationMember.organization_id == organization_id,
                OrganizationMember.user_id == user_id,
            )
            .first()
        )

    @staticmethod
    def get_organization_members(
        db: Session, organization_id: int
    ) -> list[OrganizationMember]:
        """Get all members of an organization"""
        return (
            db.query(OrganizationMember)
            .filter(OrganizationMember.organization_id == organization_id)
            .all()
        )

    @staticmethod
    def get_user_organizations(db: Session, user_id: int) -> list[OrganizationMember]:
        """Get all organizations a user belongs to"""
        return (
            db.query(OrganizationMember)
            .filter(OrganizationMember.user_id == user_id)
            .all()
        )

    @staticmethod
    def update_member_role(
        db: Session,
        organization_id: int,
        user_id: int,
        role: RoleEnum,
    ) -> OrganizationMember | None:
        """Update member role"""
        member = (
            db.query(OrganizationMember)
            .filter(
                OrganizationMember.organization_id == organization_id,
                OrganizationMember.user_id == user_id,
            )
            .first()
        )
        if not member:
            return None
        member.role = role
        db.commit()
        db.refresh(member)
        return member

    @staticmethod
    def remove_member(db: Session, organization_id: int, user_id: int) -> bool:
        """Remove member from organization"""
        member = (
            db.query(OrganizationMember)
            .filter(
                OrganizationMember.organization_id == organization_id,
                OrganizationMember.user_id == user_id,
            )
            .first()
        )
        if not member:
            return False
        db.delete(member)
        db.commit()
        return True
