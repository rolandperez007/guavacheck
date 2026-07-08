"""Database base compatibility layer."""

from __future__ import annotations

try:
    from sqlalchemy.orm import DeclarativeBase  # type: ignore
except ImportError:  # pragma: no cover - optional dependency
    class DeclarativeBase:  # type: ignore[no-redef]
        pass


class Base(DeclarativeBase):
    pass
