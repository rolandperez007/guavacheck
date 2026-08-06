"""
Country Registry

Stores country-level world intelligence.
"""


class CountryRegistry:


    def __init__(self):

        self.countries = {}


    def register(
        self,
        country,
        data,
    ):

        self.countries[country] = data


    def get(
        self,
        country,
    ):

        return self.countries.get(country)


    def all(self):

        return self.countries