from __future__ import annotations

from app.institution.services import (
    InstitutionService,
)


class Institutions:
    """
    Institution Platform facade.

    Exposes a simplified interface
    for the rest of guavacheck.
    """

    def __init__(
        self,
        service: InstitutionService,
    ) -> None:
        self.service = service