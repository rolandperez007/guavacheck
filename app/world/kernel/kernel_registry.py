class KernelRegistry:


    def __init__(self):

        self.countries = {}

        self.districts = {}

        self.engines = {}


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


    def register_engine(
        self,
        name,
        engine,
    ):

        self.engines[name] = engine