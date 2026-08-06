from uuid import UUID

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.vision.models.base import VisionBase


class Render(VisionBase):
    __tablename__ = "vision_renders"

    project_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("vision_projects.id"),
        nullable=False,
    )

    room_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("vision_rooms.id"),
        nullable=False,
    )

    image_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    provider: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    prompt: Mapped[str | None] = mapped_column(
        String(4000),
        nullable=True,
    )

    version: Mapped[int] = mapped_column(
        Integer,
        default=1,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="pending",
        nullable=False,
    )

    project = relationship(
        "VisionProject",
        back_populates="renders",
    )

    room = relationship(
        "Room",
        back_populates="renders",
    )
