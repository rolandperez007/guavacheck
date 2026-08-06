"""
Initialize Database

Creates every SQLAlchemy table.
"""

from database.base import Base
from database.connection import engine

# Import every model


async def initialize_database():

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
