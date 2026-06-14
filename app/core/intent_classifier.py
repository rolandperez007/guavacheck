# app/core/intent_classifier.py


class IntentClassifier:
    async def classify(self, text: str):
        text = text.lower()

        if "house" in text:
            return "property_search"

        if "mortgage" in text:
            return "mortgage"

        if "contractor" in text:
            return "contractor"

        return "general"
