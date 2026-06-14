class MasterPlanner:
    def generate_city(self, population):
        return {
            "population": population,
            "schools": max(1, population // 5000),
            "hospitals": max(1, population // 25000),
            "commercial_centers": max(1, population // 15000),
            "police_stations": max(1, population // 50000),
            "fire_stations": max(1, population // 50000),
            "parks": max(1, population // 10000),
            "solar_capacity_mw": population // 2000,
        }
