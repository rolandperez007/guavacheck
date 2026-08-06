from __future__ import annotations

from uuid import UUID


class BillingAdapter:
    """
    Adapter for Billing and Payments.
    """

    def create_invoice(
        self,
        institution_id: UUID,
    ):
        raise NotImplementedError

    def charge(
        self,
        institution_id: UUID,
    ):
        raise NotImplementedError

    def subscription(
        self,
        institution_id: UUID,
    ):
        raise NotImplementedError