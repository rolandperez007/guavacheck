from __future__ import annotations

from uuid import UUID


class PassportAdapter:
    """
    Adapter for the Property Passport engine.
    """

    def create_passport(
        self,
        property_id: UUID,
    ):
        """
        Create a Property Passport.
        """
        raise NotImplementedError

    def get_passport(
        self,
        passport_id: UUID,
    ):
        """
        Retrieve a Property Passport.
        """
        raise NotImplementedError

    def verify_passport(
        self,
        passport_id: UUID,
    ):
        """
        Verify passport authenticity.
        """
        raise NotImplementedError