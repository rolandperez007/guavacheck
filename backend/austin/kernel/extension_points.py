from __future__ import annotations

from typing import Any, Protocol


class OperationalExtension(Protocol):
    def attach(self, kernel: Any) -> None: ...


class ExtensionRegistry:
    def __init__(self) -> None:
        self._extensions: list[OperationalExtension] = []

    def register(self, extension: OperationalExtension) -> None:
        self._extensions.append(extension)

    def attach_all(self, kernel: Any) -> None:
        for extension in self._extensions:
            extension.attach(kernel)
