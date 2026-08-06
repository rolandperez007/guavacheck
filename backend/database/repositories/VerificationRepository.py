from database.repositories.BaseRepository import BaseRepository
from database.verification_models import VerificationRecord


class VerificationRepository(BaseRepository[VerificationRecord]):
    def __init__(self, session):

        super().__init__(session, VerificationRecord)
