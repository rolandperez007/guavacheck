"""
Engine Registry

Connects intelligence engines to the world.
"""


class EngineRegistry:


    def __init__(self):

        self.engines = {}


    def register(
        self,
        name,
        engine,
    ):

        self.engines[name] = engine


    def get(
        self,
        name,
    ):

        return self.engines.get(name)


    def all(self):

        return self.engines