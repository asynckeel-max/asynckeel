from sqlalchemy.orm import Session

from app.models.organization import Organization


class OrganizationRepository:
    """Repository for organization database operations"""

    @staticmethod
    def create_organization(
        db: Session, name: str, description: str | None, owner_id: int
    ) -> Organization:
        """Create a new organization"""
        org = Organization(
            name=name, description=description, owner_id=owner_id
        )
        db.add(org)
        db.commit()
        db.refresh(org)
        return org

    @staticmethod
    def get_organization_by_id(
        db: Session, org_id: int
    ) -> Organization | None:
        """Get organization by ID"""
        return (
            db.query(Organization)
            .filter(Organization.id == org_id)
            .first()
        )

    @staticmethod
    def get_organizations_by_owner(
        db: Session, owner_id: int, skip: int = 0, limit: int = 10
    ) -> list[Organization]:
        """Get all organizations owned by a user"""
        return (
            db.query(Organization)
            .filter(Organization.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    @staticmethod
    def update_organization(
        db: Session, org_id: int, name: str | None = None,
        description: str | None = None
    ) -> Organization | None:
        """Update organization"""
        org = (
            db.query(Organization)
            .filter(Organization.id == org_id)
            .first()
        )
        if not org:
            return None
        if name:
            org.name = name
        if description is not None:
            org.description = description
        db.commit()
        db.refresh(org)
        return org

    @staticmethod
    def delete_organization(db: Session, org_id: int) -> bool:
        """Delete organization"""
        org = (
            db.query(Organization)
            .filter(Organization.id == org_id)
            .first()
        )
        if not org:
            return False
        db.delete(org)
        db.commit()
        return True

    @staticmethod
    def get_all_organizations(
        db: Session, skip: int = 0, limit: int = 10
    ) -> list[Organization]:
        """Get all organizations"""
        return (
            db.query(Organization)
            .offset(skip)
            .limit(limit)
            .all()
        )
