from database.audit_models import AuditLog
from database.repositories.BaseRepository import BaseRepository


class AuditRepository(BaseRepository[AuditLog]):
    def __init__(self, session):

        super().__init__(session, AuditLog)
