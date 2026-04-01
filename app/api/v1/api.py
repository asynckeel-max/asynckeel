from fastapi import APIRouter

from app.api.v1.endpoints import auth, users, organizations, organization_members, api_keys

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(auth.router)
api_router.include_router(users.router)
api_router.include_router(organizations.router)
api_router.include_router(organization_members.router)
api_router.include_router(api_keys.router)
