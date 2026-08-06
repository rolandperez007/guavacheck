from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.vision.models.base import VisionBase


class VisionProject(VisionBase):
    __tablename__ = "vision_projects"

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    owner_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
        index=True,
    )

    property_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    design_style: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    budget: Mapped[int] = mapped_column(
        Integer,
        nullable=True,
    )

    location: Mapped[str] = mapped_column(
        String(255),
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="draft",
    )

    rooms = relationship(
        "Room",
        back_populates="project",
        cascade="all, delete-orphan",
    )

    renders = relationship(
        "Render",
        back_populates="project",
        cascade="all, delete-orphan",
    )
