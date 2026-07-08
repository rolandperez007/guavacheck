"""
Initialize Database

Creates every SQLAlchemy table.
"""

from database.connection import engine
from database.base import Base

# Import every model

import database.models


async def initialize_database():

    async with engine.begin() as conn:

        await conn.run_sync(Base.metadata.create_all)
