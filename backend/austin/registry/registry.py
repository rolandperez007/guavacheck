"""
Austin Engine Registry

Central runtime registry for Austin engines.

Responsibilities
----------------
- Boot the registry
- Discover engine manifests
- Load engine instances
- Register engines
- Index by intent
- Index by capability
- Provide runtime lookup
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass

from backend.austin.registry.manifests.base import EngineManifest
from backend.austin.registry.loader import loader
from .discovery import engine_discovery

@dataclass(slots=True)
class EngineRecord:
    manifest: EngineManifest
    engine: object


class AustinRegistry:

    def __init__(self):

        self._records: dict[str, EngineRecord] = {}

        self._intent_index: dict[str, list[EngineRecord]] = (
            defaultdict(list)
        )

        self._capability_index: dict[
            str,
            list[EngineRecord],
        ] = defaultdict(list)

        self._booted = False

    # ---------------------------------------------------------
    # Boot
    # ---------------------------------------------------------

    def boot(self) -> None:

        if self._booted:
            return

        manifests = engine_discovery.discover()

        for manifest in manifests:

            self.register(manifest)

        self._booted = True

    # ---------------------------------------------------------
    # Shutdown
    # ---------------------------------------------------------

    def shutdown(self) -> None:

        loader.unload_all()

        self._records.clear()

        self._intent_index.clear()

        self._capability_index.clear()

        self._booted = False

    # ---------------------------------------------------------
    # Registration
    # ---------------------------------------------------------

    def register(
        self,
        manifest: EngineManifest,
    ) -> None:

        if not manifest.enabled:
            return

        engine = loader.load(manifest)

        record = EngineRecord(

            manifest=manifest,

            engine=engine,

        )

        self._records[manifest.name] = record

        for intent in manifest.intents:

            self._intent_index[intent].append(
                record
            )

        for capability in manifest.capabilities:

            self._capability_index[
                capability
            ].append(record)

    # ---------------------------------------------------------
    # Engine Lookup
    # ---------------------------------------------------------

    def get(
        self,
        name: str,
    ) -> object | None:

        record = self._records.get(name)

        if record:

            return record.engine

        return None

    def manifest(
        self,
        name: str,
    ) -> EngineManifest | None:

        record = self._records.get(name)

        if record:

            return record.manifest

        return None

    # ---------------------------------------------------------
    # Intent Lookup
    # ---------------------------------------------------------

    def find_by_intent(
        self,
        intent: str,
    ) -> list[object]:

        return [

            record.engine

            for record in self._intent_index.get(
                intent,
                [],
            )

        ]

    # ---------------------------------------------------------
    # Capability Lookup
    # ---------------------------------------------------------

    def find_by_capability(
        self,
        capability: str,
    ) -> list[object]:

        return [

            record.engine

            for record in self._capability_index.get(
                capability,
                [],
            )

        ]

    # ---------------------------------------------------------
    # Listing
    # ---------------------------------------------------------

    def list_engines(self) -> list[str]:

        return sorted(

            self._records.keys()

        )

    def manifests(self) -> list[EngineManifest]:

        return [

            record.manifest

            for record in self._records.values()

        ]

    # ---------------------------------------------------------
    # Statistics
    # ---------------------------------------------------------

    def count(self) -> int:

        return len(self._records)

    @property
    def booted(self) -> bool:

        return self._booted

    # ---------------------------------------------------------
    # Diagnostics
    # ---------------------------------------------------------

    def health(self) -> dict:

        return {

            "booted": self._booted,

            "engine_count": self.count(),

            "engines": self.list_engines(),

            "intents": len(self._intent_index),

            "capabilities": len(
                self._capability_index
            ),

        }


registry = AustinRegistry()