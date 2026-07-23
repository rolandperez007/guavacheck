"""
Austin Engine Discovery

Discovers all valid Austin engine manifests.
"""

from __future__ import annotations

import importlib
import pkgutil
from pathlib import Path


class EngineDiscovery:

    def __init__(self):

        self.package = "backend.austin.registry.manifests"

    def discover(self):

        manifests = []

        package = importlib.import_module(self.package)

        package_path = Path(package.__file__).parent

        for module_info in pkgutil.iter_modules([str(package_path)]):

            if module_info.name.startswith("_"):

                continue

            module = importlib.import_module(
                f"{self.package}.{module_info.name}"
            )

            manifest = (
                getattr(module, "MANIFEST", None)
                or getattr(module, "manifest", None)
            )

            if manifest is not None:

                manifests.append(manifest)

        return manifests


engine_discovery = EngineDiscovery()