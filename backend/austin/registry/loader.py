"""
Austin Engine Loader

Responsible for importing and instantiating Austin engines.

The loader never stores engines.
The loader never performs discovery.
The loader only converts a manifest entry into a live engine instance.
"""

from __future__ import annotations

import importlib

from backend.austin.registry.manifests.base import EngineManifest


class EngineLoader:
    """
    Loads engine classes from manifests.
    """

    def __init__(self):

        self._cache: dict[str, object] = {}

    # ---------------------------------------------------------
    # Public
    # ---------------------------------------------------------

    def load(
        self,
        manifest: EngineManifest,
    ) -> object:

        if manifest.name in self._cache:
            return self._cache[manifest.name]

        engine = self._instantiate(manifest.engine_class)

        self._cache[manifest.name] = engine

        return engine

    def unload(
        self,
        name: str,
    ) -> None:

        self._cache.pop(name, None)

    def unload_all(self) -> None:

        self._cache.clear()

    def loaded(self) -> list[str]:

        return sorted(self._cache.keys())

    # ---------------------------------------------------------
    # Internal
    # ---------------------------------------------------------

    def _instantiate(
        self,
        class_path: str,
    ) -> object:

        if "." not in class_path:
            raise RuntimeError(f"Invalid engine path: {class_path}")

        module_path, class_name = class_path.rsplit(".", 1)

        module = importlib.import_module(module_path)

        engine_class = getattr(
            module,
            class_name,
        )

        return engine_class()


loader = EngineLoader()
