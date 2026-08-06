"""
District Loader

Creates district instances
and registers them into the World Registry.
"""


class DistrictLoader:


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
        country,
        template,
        override,
    ):


        district = self.generator.create(

            name,

            country,

            template,

            override,

        )


        self.registry.register_district(

            name,

            district.data,

        )


        return district