from app.database.base import Base
from app.database.session import engine

# Import all models so SQLAlchemy knows them
import app.database.registry


def create_tables():

    Base.metadata.create_all(
        bind=engine
    )


if __name__ == "__main__":

    create_tables()

    print(
        "Database tables created successfully"
    )