"""
Austin World Kernel

Central runtime coordinator.

Responsible for:

- Booting World Runtime
- Holding Registry connection
- Resolving world intelligence
"""


class WorldKernel:


    def __init__(
        self,
        runtime=None,
        registry=None,
    ):

        self.runtime = runtime

        self.registry = registry

        self.status = "initialized"



    def boot(self):

        self.status = "running"

        return {

            "kernel": "world",

            "status": self.status,

            "registry_connected":
                self.registry is not None,

        }



    def resolve_location(
        self,
        country,
        district=None,
    ):


        country_data = None

        district_data = None


        if self.registry:

            country_data = (
                self.registry
                .get_country(country)
            )


            if district:

                district_data = (
                    self.registry
                    .get_district(district)
                )


        return {

            "country": country,

            "country_data": country_data,

            "district": district,

            "district_data": district_data,

        }
