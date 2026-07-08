from database.repositories.BaseRepository import BaseRepository

from database.document_models import DocumentRecord


class DocumentRepository(

    BaseRepository[DocumentRecord]

):

    def __init__(self, session):

        super().__init__(

            session,

            DocumentRecord

        )
