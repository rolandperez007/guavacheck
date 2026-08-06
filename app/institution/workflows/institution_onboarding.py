from __future__ import annotations

from app.institution.models import Institution
from app.institution.services import (
    InstitutionService,
)


class InstitutionOnboardingWorkflow:
    """
    Coordinates the complete onboarding
    lifecycle for a new institution.
    """

    def __init__(
        self,
        service: InstitutionService,
    ) -> None:
        self.service = service

    def onboard(
        self,
        institution: Institution,
    ) -> Institution:
        """
        Complete onboarding pipeline.
        """

        institution = self.service.create(
            institution,
        )

        self.service.verify(
            institution.id,
        )

        return institution