"""
World Loader

Loads structured world data into the World Registry.
"""


class WorldLoader:


    def __init__(
        self,
        registry,
    ):

        self.registry = registry



    def load_country(
        self,
        name,
        data,
    ):

        self.registry.register_country(
            name,
            data,
        )



    def load_district(
        self,
        name,
        data,
    ):

        self.registry.register_district(
            name,
            data,
        )



    def load_engine(
        self,
        name,
        engine,
    ):

        self.registry.register_engine(
            name,
            engine,
        )