from sqlalchemy.orm import Session


class BaseRepository:
    def __init__(self, db: Session):
        self.db = db

    def add(self, entity):
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def delete(self, entity):
        self.db.delete(entity)
        self.db.commit()

    def commit(self):
        self.db.commit()

    def refresh(self, entity):
        self.db.refresh(entity)
