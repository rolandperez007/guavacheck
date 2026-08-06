from __future__ import annotations

from app.institution.services import VerificationService


class VerificationTask:
    """
    Executes pending verification jobs.
    """

    def __init__(
        self,
        service: VerificationService,
    ) -> None:
        self.service = service

    def run(self) -> None:
        pending = self.service.pending()

        for institution in pending:
            self.service.verify(institution.id)