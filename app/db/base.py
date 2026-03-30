from sqlalchemy.orm import declarative_base

Base = declarative_base()

from app.models.api_key import ApiKey  # noqa: F401, E402
from app.models.organization import Organization  # noqa: F401, E402
from app.models.organization_member import (  # noqa: F401, E402
    OrganizationMember,
)

# Import models AFTER Base is created to avoid circular imports
from app.models.user import User  # noqa: F401, E402
