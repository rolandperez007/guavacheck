"""
World Registry

Central knowledge registry for Austin's World Runtime.

Coordinates:

- Countries
- Districts
- Intelligence Engines
"""


from app.world.registry.country_registry import CountryRegistry
from app.world.registry.district_registry import DistrictRegistry
from app.world.registry.engine_registry import EngineRegistry



class WorldRegistry:


    def __init__(self):

        self.countries = CountryRegistry()

        self.districts = DistrictRegistry()

        self.engines = EngineRegistry()



    def register_country(
        self,
        name,
        data,
    ):

        self.countries.register(
            name,
            data,
        )



    def register_district(
        self,
        name,
        data,
    ):

        self.districts.register(
            name,
            data,
        )



    def register_engine(
        self,
        name,
        engine,
    ):

        self.engines.register(
            name,
            engine,
        )



    def get_country(
        self,
        name,
    ):

        return self.countries.get(
            name
        )



    def get_district(
        self,
        name,
    ):

        return self.districts.get(
            name
        )



    def get_engine(
        self,
        name,
    ):

        return self.engines.get(
            name
        )