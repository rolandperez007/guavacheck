"""
Base Repository

Provides common CRUD functionality for every repository.

Author: guavacheck
"""

from __future__ import annotations

from typing import Generic, TypeVar

try:
    from sqlalchemy import select
    from sqlalchemy.ext.asyncio import AsyncSession
except ImportError:  # pragma: no cover - optional dependency
    select = None
    AsyncSession = object


ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    def __init__(
        self,
        session: AsyncSession,
        model: type[ModelType],
    ):
        self.session = session
        self.model = model

    async def create(self, obj: ModelType):

        self.session.add(obj)

        await self.session.commit()

        await self.session.refresh(obj)

        return obj

    async def get_by_id(self, id_value):
        if select is None:
            raise RuntimeError("SQLAlchemy is required to use BaseRepository")

        result = await self.session.execute(
            select(self.model).where(self.model.id == id_value)
        )

        return result.scalar_one_or_none()

    async def get_all(self) -> list[ModelType]:
        if select is None:
            raise RuntimeError("SQLAlchemy is required to use BaseRepository")

        result = await self.session.execute(select(self.model))

        return result.scalars().all()

    async def delete(self, obj):

        await self.session.delete(obj)

        await self.session.commit()

    async def update(self):

        await self.session.commit()

    async def exists(self, id_value):

        return await self.get_by_id(id_value) is not None
