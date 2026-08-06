from __future__ import annotations

from app.institution.models import Institution


class InstitutionValidator:
    """
    Business validation rules for institutions.
    """

    @staticmethod
    def validate(institution: Institution) -> None:
        if not institution.legal_name:
            raise ValueError("Legal name is required.")

        if not institution.registration_number:
            raise ValueError(
                "Registration number is required."
            )

        if not institution.email:
            raise ValueError("Email is required.")