from database.repositories.BaseRepository import BaseRepository

from database.audit_models import AuditLog


class AuditRepository(

    BaseRepository[AuditLog]

):

    def __init__(self, session):

        super().__init__(

            session,

            AuditLog

        )
