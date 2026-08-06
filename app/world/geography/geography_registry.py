"""
Geography Registry

Stores the global location graph.
"""


class GeographyRegistry:


    def __init__(self):

        self.locations = {}


    def add(
        self,
        location,
    ):

        self.locations[
            location.name
        ] = location


    def get(
        self,
        name,
    ):

        return self.locations.get(
            name
        )


    def all(self):

        return self.locations