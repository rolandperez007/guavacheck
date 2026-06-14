class DesignBrain:
    def generate(self, project):
        return {
            "asset_type": project["asset_type"],
            "floors": 5,
            "rooms": 100,
            "parking_spaces": 50,
            "land_area_sqm": 5000,
            "design_status": "concept",
        }
