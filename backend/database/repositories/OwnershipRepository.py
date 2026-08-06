from database.ownership_models import OwnershipRecord
from database.repositories.BaseRepository import BaseRepository


class OwnershipRepository(BaseRepository[OwnershipRecord]):
    def __init__(self, session):

        super().__init__(session, OwnershipRecord)
