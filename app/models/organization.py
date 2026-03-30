from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class Organization(Base):
    """Organization model for database"""

    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    description = Column(String(500), nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    # Relationships
    owner = relationship(
        "User",
        back_populates="organizations",
        foreign_keys=[owner_id],
    )
    members = relationship("OrganizationMember", back_populates="organization")
    api_keys = relationship("ApiKey", back_populates="organization")

    def __repr__(self):
        return (
            f"<Organization(id={self.id}, name={self.name}, "
            f"owner_id={self.owner_id})>"
        )
