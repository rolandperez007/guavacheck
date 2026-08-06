"""
Austin Engine Registry

Maintains the collection of
available runtime engines.
"""


class EngineRegistry:

    def __init__(self):
        self._engines = {}

    def register(
        self,
        name,
        engine,
    ):
        self._engines[name] = engine

    def get(
        self,
        name,
    ):
        return self._engines.get(name)

    def exists(
        self,
        name,
    ):
        return name in self._engines

    def names(self):
        return sorted(self._engines.keys())

    def summary(self):
        return {
            "engines": len(self._engines),
            "names": self.names(),
        }