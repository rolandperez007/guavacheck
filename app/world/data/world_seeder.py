"""
World Seeder

Loads world data files and
registers them into the runtime.
"""


from pathlib import Path


from app.world.data import YAMLWorldLoader



class WorldSeeder:


    def __init__(
        self,
        registry,
        loader=None,
    ):

        self.registry = registry

        self.loader = loader or YAMLWorldLoader()



    def seed_countries(
        self,
        path="docs/world/countries",
    ):


        directory = Path(path)


        for file in directory.glob("*.yaml"):


            data = self.loader.load_file(
                file
            )


            self.registry.register_country(

                data["name"],

                data,

            )



    def seed_districts(
        self,
        path="docs/world/districts",
    ):


        directory = Path(path)


        for file in directory.glob("*.yaml"):


            data = self.loader.load_file(
                file
            )


            self.registry.register_district(

                data["name"],

                data,

            )



    def seed(
        self,
    ):


        self.seed_countries()


        self.seed_districts()


        return self.registry.summary()