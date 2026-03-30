from sqlalchemy.orm import declarative_base

from app.models.user import User
from app.models.organization import Organization
from app.models.organization_member import OrganizationMember
from app.models.api_key import ApiKey

Base = declarative_base()
