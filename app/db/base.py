from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import models to register them with Base
from app.models.user import User  # noqa: F401
from app.models.organization import Organization  # noqa: F401
from app.models.organization_member import (  # noqa: F401
    OrganizationMember,
)
from app.models.api_key import ApiKey  # noqa: F401
