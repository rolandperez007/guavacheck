class RankingAgent:

    def score(self, property_data):

        score = 75

        if property_data.get("location") == "Lekki":
            score += 10

        return score