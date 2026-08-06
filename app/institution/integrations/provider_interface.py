from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class InstitutionProvider(ABC):
    """
    Base interface for every external institution
    integration.

    Banks, insurers, governments,
    valuation firms, developers,
    law firms and other providers
    implement this contract.
    """

    @abstractmethod
    def authenticate(self) -> bool:
        """
        Authenticate with the provider.
        """

    @abstractmethod
    def health_check(self) -> bool:
        """
        Verify provider availability.
        """

    @abstractmethod
    def synchronize(self) -> None:
        """
        Synchronize provider data.
        """

    @abstractmethod
    def publish_product(
        self,
        product_id: str,
    ) -> None:
        """
        Publish a product.
        """

    @abstractmethod
    def publish_service(
        self,
        service_id: str,
    ) -> None:
        """
        Publish a service.
        """

    @abstractmethod
    def publish_offer(
        self,
        offer_id: str,
    ) -> None:
        """
        Publish a commercial offer.
        """

    @abstractmethod
    def verify_customer(
        self,
        customer_id: str,
    ) -> bool:
        """
        Verify a customer.
        """

    @abstractmethod
    def create_subscription(
        self,
        subscription_id: str,
    ) -> None:
        """
        Create a provider subscription.
        """

    @abstractmethod
    def cancel_subscription(
        self,
        subscription_id: str,
    ) -> None:
        """
        Cancel a provider subscription.
        """