"""
District Generator

Creates district intelligence
from templates and local overrides.
"""


from app.world.districts.district_instance import DistrictInstance



class DistrictGenerator:


    def __init__(
        self,
        template_engine,
    ):

        self.template_engine = template_engine



    def create(
        self,
        name,
        country,
        template,
        override,
    ):


        district_data = (
            self.template_engine.merge(
                template,
                override,
            )
        )


        return DistrictInstance(

            name=name,

            country=country,

            data=district_data,

        )