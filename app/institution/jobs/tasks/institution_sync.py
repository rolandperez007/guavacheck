from __future__ import annotations

from app.institution.services import InstitutionService


class InstitutionSyncTask:
    """
    Synchronizes institutions with
    external providers.
    """

    def __init__(
        self,
        service: InstitutionService,
    ) -> None:
        self.service = service

    def run(self) -> None:
        """
        Synchronize every registered institution.
        """
        institutions = self.service.list_all()

        for institution in institutions:
            self.service.sync(institution.id)