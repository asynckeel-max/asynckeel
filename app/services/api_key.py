from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.core.exceptions import (
    NotFoundException,
    UnauthorizedException,
)
from app.core.security import (
    generate_api_key,
    hash_api_key,
    verify_api_key,
)
from app.models.organization_member import RoleEnum
from app.repositories.api_key import ApiKeyRepository
from app.repositories.organization_member import (
    OrganizationMemberRepository,
)
from app.schemas.api_key import ApiKeyCreate


class ApiKeyService:
    """Service for API key operations"""

    @staticmethod
    def create_api_key(
        db: Session,
        org_id: int,
        user_id: int,
        api_key_data: ApiKeyCreate,
        expires_in_days: int = 90,
    ):
        """Create a new API key (only admin/owner can create)"""
        # Check if user is admin or owner
        member = OrganizationMemberRepository.get_member(
            db, org_id, user_id
        )
        if not member or member.role not in [
            RoleEnum.OWNER,
            RoleEnum.ADMIN,
        ]:
            raise UnauthorizedException(
                "Only owner or admin can create API keys"
            )

        # Generate API key
        plain_key = generate_api_key()
        key_hash = hash_api_key(plain_key)

        # Calculate expiration
        expires_at = datetime.utcnow() + timedelta(days=expires_in_days)

        # Create API key in database
        api_key = ApiKeyRepository.create_api_key(
            db, org_id, api_key_data.name, key_hash
        )

        # Update expiration
        api_key.expires_at = expires_at
        db.commit()
        db.refresh(api_key)

        # Return both key and hash (key only shown once)
        return {"api_key": api_key, "plain_key": plain_key}

    @staticmethod
    def get_api_key(db: Session, org_id: int, user_id: int, key_id: int):
        """Get API key details (only admin/owner can view)"""
        # Check if user is admin or owner
        member = OrganizationMemberRepository.get_member(
            db, org_id, user_id
        )
        if not member or member.role not in [
            RoleEnum.OWNER,
            RoleEnum.ADMIN,
        ]:
            raise UnauthorizedException(
                "Only owner or admin can view API keys"
            )

        api_key = ApiKeyRepository.get_api_key_by_id(db, key_id)
        if not api_key or api_key.organization_id != org_id:
            raise NotFoundException("API key not found")

        return api_key

    @staticmethod
    def list_api_keys(db: Session, org_id: int, user_id: int):
        """List all API keys for organization"""
        # Check if user is member
        member = OrganizationMemberRepository.get_member(
            db, org_id, user_id
        )
        if not member:
            raise UnauthorizedException(
                "User is not a member of this organization"
            )

        return ApiKeyRepository.get_organization_api_keys(db, org_id)

    @staticmethod
    def revoke_api_key(
        db: Session, org_id: int, user_id: int, key_id: int
    ):
        """Revoke API key (only admin/owner can revoke)"""
        # Check if user is admin or owner
        member = OrganizationMemberRepository.get_member(
            db, org_id, user_id
        )
        if not member or member.role not in [
            RoleEnum.OWNER,
            RoleEnum.ADMIN,
        ]:
            raise UnauthorizedException(
                "Only owner or admin can revoke API keys"
            )

        api_key = ApiKeyRepository.get_api_key_by_id(db, key_id)
        if not api_key or api_key.organization_id != org_id:
            raise NotFoundException("API key not found")

        # Deactivate key
        return ApiKeyRepository.update_api_key(
            db, key_id, is_active=False
        )

    @staticmethod
    def verify_and_use_api_key(db: Session, plain_key: str):
        """Verify API key and mark as used"""
        key_hash = hash_api_key(plain_key)
        api_key = ApiKeyRepository.get_api_key_by_hash(db, key_hash)

        if not api_key:
            raise NotFoundException("Invalid API key")

        if not api_key.is_active:
            raise UnauthorizedException("API key is revoked")

        # Check expiration
        if api_key.expires_at and datetime.utcnow() > api_key.expires_at:
            raise UnauthorizedException("API key has expired")

        # Mark as used
        ApiKeyRepository.mark_api_key_used(db, api_key.id)

        return api_key
