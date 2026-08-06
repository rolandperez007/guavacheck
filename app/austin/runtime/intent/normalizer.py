"""
Austin Intent Normalizer

Transforms raw user input
into structured intent data.
"""


class IntentNormalizer:


    def __init__(
        self,
    ):

        self.corrections = {

            "loasd": "load",

            "creat": "create",

            "propety": "property",

            "analysys": "analysis",

            "procees": "process",

        }



    def normalize_text(
        self,
        text,
    ):


        words = text.lower().split()


        normalized = []


        for word in words:


            normalized.append(

                self.corrections.get(

                    word,

                    word,

                )

            )


        return " ".join(
            normalized
        )



    def detect_intent(
        self,
        text,
    ):


        normalized = self.normalize_text(
            text
        )


        intent = "unknown"


        if "load" in normalized:

            intent = "load"



        elif "create" in normalized:

            intent = "create"



        elif "property" in normalized:

            intent = "property"



        return {

            "input": text,

            "normalized": normalized,

            "intent": intent,

        }