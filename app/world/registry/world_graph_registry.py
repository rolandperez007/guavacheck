"""
World Graph Registry

Unified registry for:

Countries
Districts
Geography
"""


class WorldGraphRegistry:


    def __init__(self):

        self.countries = {}

        self.districts = {}

        self.locations = {}



    def register_country(
        self,
        name,
        data,
    ):

        self.countries[name] = data



    def register_district(
        self,
        name,
        data,
    ):

        self.districts[name] = data



    def register_location(
        self,
        location,
    ):

        self.locations[
            location.name
        ] = location



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



    def get_location(
        self,
        name,
    ):

        return self.locations.get(
            name
        )



    def summary(self):

        return {

            "countries": len(
                self.countries
            ),

            "districts": len(
                self.districts
            ),

            "locations": len(
                self.locations
            ),

        }