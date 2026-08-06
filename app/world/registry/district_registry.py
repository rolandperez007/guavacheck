"""
District Registry

Stores geographic intelligence zones.
"""


class DistrictRegistry:


    def __init__(self):

        self.districts = {}


    def register(
        self,
        district,
        data,
    ):

        self.districts[district] = data


    def get(
        self,
        district,
    ):

        return self.districts.get(district)


    def all(self):

        return self.districts