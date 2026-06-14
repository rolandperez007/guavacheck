class CostEngine:
    def estimate(self, boq):
        total = boq["cement_bags"] * 15 + boq["blocks"] * 1 + boq["steel_tons"] * 1200

        return {"estimated_cost": total, "currency": "USD"}
