from __future__ import annotations

from sqlalchemy.orm import Session

from app.institution.models.product import Product
from app.institution.repositories.product_repository import (
    ProductRepository,
)
from app.institution.services.base_service import BaseService


class ProductService(BaseService):
    """
    Application service for institution products.
    """

    def __init__(
        self,
        db: Session,
    ):
        super().__init__(db)

        self.products = ProductRepository(db)

    def create(
        self,
        product: Product,
    ) -> Product:
        """
        Create a new institution product.
        """

        self.products.add(product)

        self.commit()

        self.db.refresh(product)

        return product

    def get(
        self,
        product_id: str,
    ) -> Product | None:
        return self.products.get(product_id)

    def list(
        self,
    ) -> list[Product]:
        return self.products.list()

    def list_by_institution(
        self,
        institution_id: str,
    ) -> list[Product]:
        return self.products.list_by_institution(
            institution_id,
        )