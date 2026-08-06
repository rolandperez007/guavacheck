from app.institution.repositories import (
    InstitutionRepository,
)
from app.institution.services import (
    InstitutionService,
)


def get_repository() -> InstitutionRepository:
    return InstitutionRepository()


def get_service() -> InstitutionService:
    repository = get_repository()

    return InstitutionService(
        repository=repository,
    )