class PricingAgent:

    def analyze(self, property_data):

        return {
            "estimated_value": property_data.get("price"),
            "confidence": 0.82
        }