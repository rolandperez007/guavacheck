"""
guavacheck Database Connection

Enterprise SQLAlchemy configuration.

Supports:

- PostgreSQL
- Supabase
- AsyncPG
- Alembic
- Connection Pooling
"""

from __future__ import annotations

import os

try:
    from sqlalchemy.ext.asyncio import (  # type: ignore
        create_async_engine,
        AsyncSession,
    )
    from sqlalchemy.orm import sessionmaker  # type: ignore
except ImportError:  # pragma: no cover - optional dependency
    create_async_engine = None  # type: ignore[assignment]
    AsyncSession = None  # type: ignore[assignment]
    sessionmaker = None  # type: ignore[assignment]

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://postgres:postgres@localhost/guavacheck",
)

engine = None
SessionLocal = None

if create_async_engine is not None and sessionmaker is not None and AsyncSession is not None:
    engine = create_async_engine(
        DATABASE_URL,
        echo=False,
        future=True,
        pool_size=20,
        max_overflow=40,
        pool_pre_ping=True,
    )

    SessionLocal = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )


def get_connection():
    return engine


# Compatibility: lightweight database object used by older modules
class _DatabaseCompat:
    def __init__(self):
        self.connected = False

    def connect(self):
        # No-op compatibility in environments without SQLAlchemy
        self.connected = True

    def disconnect(self):
        self.connected = False


database = _DatabaseCompat()
