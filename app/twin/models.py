from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.constants import STATUS_LENGTH
from app.db.mixins import TimestampMixin, UUIDMixin


class Twin(
    UUIDMixin,
    TimestampMixin,
    Base,
):
    """
    Digital representation of a physical property.
    """

    __tablename__ = "twins"

    property_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
        index=True,
    )

    passport_id: Mapped[str | None] = mapped_column(
        String(36),
        nullable=True,
    )

    owner_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
        index=True,
    )

    status: Mapped[str] = mapped_column(
        String(STATUS_LENGTH),
        default="active",
        nullable=False,
    )

    version: Mapped[int] = mapped_column(
        Integer,
        default=1,
        nullable=False,
    )
