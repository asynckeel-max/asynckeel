from sqlalchemy.orm import Session

from app.models.api_key import ApiKey


class ApiKeyRepository:
    """Repository for API key operations"""

    @staticmethod
    def create_api_key(
        db: Session,
        organization_id: int,
        name: str,
        key_hash: str,
    ) -> ApiKey:
        """Create a new API key"""
        api_key = ApiKey(
            organization_id=organization_id,
            name=name,
            key_hash=key_hash,
        )
        db.add(api_key)
        db.commit()
        db.refresh(api_key)
        return api_key

    @staticmethod
    def get_api_key_by_id(db: Session, api_key_id: int) -> ApiKey | None:
        """Get API key by ID"""
        return db.query(ApiKey).filter(ApiKey.id == api_key_id).first()

    @staticmethod
    def get_api_key_by_hash(db: Session, key_hash: str) -> ApiKey | None:
        """Get API key by hash"""
        return db.query(ApiKey).filter(ApiKey.key_hash == key_hash).first()

    @staticmethod
    def get_organization_api_keys(db: Session, organization_id: int) -> list[ApiKey]:
        """Get all API keys for an organization"""
        return db.query(ApiKey).filter(ApiKey.organization_id == organization_id).all()

    @staticmethod
    def update_api_key(
        db: Session,
        api_key_id: int,
        name: str | None = None,
        is_active: bool | None = None,
    ) -> ApiKey | None:
        """Update API key"""
        api_key = db.query(ApiKey).filter(ApiKey.id == api_key_id).first()
        if not api_key:
            return None
        if name:
            api_key.name = name
        if is_active is not None:
            api_key.is_active = is_active
        db.commit()
        db.refresh(api_key)
        return api_key

    @staticmethod
    def delete_api_key(db: Session, api_key_id: int) -> bool:
        """Delete API key"""
        api_key = db.query(ApiKey).filter(ApiKey.id == api_key_id).first()
        if not api_key:
            return False
        db.delete(api_key)
        db.commit()
        return True

    @staticmethod
    def mark_api_key_used(db: Session, api_key_id: int) -> ApiKey | None:
        """Mark API key as used"""
        from datetime import datetime

        api_key = db.query(ApiKey).filter(ApiKey.id == api_key_id).first()
        if not api_key:
            return None
        api_key.last_used_at = datetime.utcnow()
        db.commit()
        db.refresh(api_key)
        return api_key
