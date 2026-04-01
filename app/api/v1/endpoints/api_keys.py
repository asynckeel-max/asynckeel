from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user, get_db
from app.models.user import User
from app.schemas.api_key import (
    ApiKeyCreate,
    ApiKeyCreateResponse,
    ApiKeyResponse,
)
from app.services.api_key import ApiKeyService

router = APIRouter(
    prefix="/organizations/{org_id}/api-keys",
    tags=["api-keys"],
)


@router.post(
    "",
    response_model=ApiKeyCreateResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_api_key(
    org_id: int,
    api_key_data: ApiKeyCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Create a new API key (admin/owner only)"""
    result = ApiKeyService.create_api_key(db, org_id, current_user.id, api_key_data)
    api_key = result["api_key"]
    plain_key = result["plain_key"]

    return ApiKeyCreateResponse(
        id=api_key.id,
        organization_id=api_key.organization_id,
        name=api_key.name,
        key=plain_key,
        created_at=api_key.created_at,
    )


@router.get("", response_model=list[ApiKeyResponse])
def list_api_keys(
    org_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """List all API keys for organization"""
    return ApiKeyService.list_api_keys(db, org_id, current_user.id)


@router.get("/{key_id}", response_model=ApiKeyResponse)
def get_api_key(
    org_id: int,
    key_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get API key details (admin/owner only)"""
    return ApiKeyService.get_api_key(db, org_id, current_user.id, key_id)


@router.delete("/{key_id}", status_code=status.HTTP_204_NO_CONTENT)
def revoke_api_key(
    org_id: int,
    key_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Revoke API key (admin/owner only)"""
    ApiKeyService.revoke_api_key(db, org_id, current_user.id, key_id)
