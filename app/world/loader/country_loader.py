"""
Country Loader

Creates country instances
and registers them into the World Registry.
"""


class CountryLoader:


    def __init__(
        self,
        generator,
        registry,
    ):

        self.generator = generator

        self.registry = registry



    def load(
        self,
        name,
        template,
        override,
    ):


        country = self.generator.create(

            name,

            template,

            override,

        )


        self.registry.register_country(

            name,

            country.data,

        )


        return country