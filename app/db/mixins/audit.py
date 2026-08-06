from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.constants import UUID_LENGTH


class AuditMixin:
    """
    Tracks who created and modified a record.

    IRONGATE will populate these fields.
    """

    created_by: Mapped[str | None] = mapped_column(
        String(UUID_LENGTH),
        nullable=True,
    )

    updated_by: Mapped[str | None] = mapped_column(
        String(UUID_LENGTH),
        nullable=True,
    )
