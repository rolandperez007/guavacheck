"""
Create all database tables.

This module uses the canonical SQLAlchemy Base and registry.
"""

from app.db.base import Base
from app.db.session import engine

# Importing the canonical registry registers all ORM models.
import app.db.registry  # noqa: F401


def create_tables() -> None:
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")


if __name__ == "__main__":
    create_tables()
