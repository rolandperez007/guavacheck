from __future__ import annotations

from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.mixins import TimestampMixin


class ProductService(
    TimestampMixin,
    Base,
):
    """
    Associates Products with Services.

    Example:

    Mortgage Product
        ├── Property Valuation
        ├── Legal Review
        ├── Survey
        └── Insurance
    """

    __tablename__ = "institution_product_services"

    product_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey(
            "institution_products.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    service_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey(
            "institution_services.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )
