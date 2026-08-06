"""
World Runtime Boot Report
"""


class BootReport:


    def __init__(
        self,
        state,
    ):

        self.state = state


    def generate(self):

        return {

            "status": self.state.status,

            "countries":
                self.state.countries_loaded,

            "districts":
                self.state.districts_loaded,

            "engines":
                self.state.engines_connected,

        }