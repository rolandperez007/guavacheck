from __future__ import annotations

from sqlalchemy.orm import Session

from app.institution.models.product import Product
from app.institution.repositories.base_repository import BaseRepository


class ProductRepository(BaseRepository[Product]):
    """
    Repository for Institution Products.
    """

    def __init__(self, db: Session):
        super().__init__(db)

    def get(
        self,
        product_id: str,
    ) -> Product | None:
        return (
            self.db.query(Product)
            .filter(Product.id == product_id)
            .first()
        )

    def list(self) -> list[Product]:
        return (
            self.db.query(Product)
            .all()
        )

    def list_by_institution(
        self,
        institution_id: str,
    ) -> list[Product]:
        return (
            self.db.query(Product)
            .filter(
                Product.institution_id == institution_id
            )
            .all()
        )