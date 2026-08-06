"""
Country Generator

Creates country intelligence
from templates and overrides.
"""


from app.world.countries.country_instance import CountryInstance



class CountryGenerator:


    def __init__(
        self,
        template_engine,
    ):

        self.template_engine = template_engine



    def create(
        self,
        name,
        template,
        override,
    ):


        country_data = (
            self.template_engine.merge(
                template,
                override,
            )
        )


        return CountryInstance(

            name=name,

            data=country_data,

        )