from database.document_models import DocumentRecord
from database.repositories.BaseRepository import BaseRepository


class DocumentRepository(BaseRepository[DocumentRecord]):
    def __init__(self, session):

        super().__init__(session, DocumentRecord)
