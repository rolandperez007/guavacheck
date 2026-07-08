from database.repositories.BaseRepository import BaseRepository

from database.property_models import PropertyRecord


class PropertyRepository(

    BaseRepository[PropertyRecord]

):

    def __init__(self, session):

        super().__init__(

            session,

            PropertyRecord

        )
