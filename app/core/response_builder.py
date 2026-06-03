class ResponseBuilder:

    def build(
        self,
        input_text,
        intent,
        data
    ):

        return {
            "input": input_text,
            "intent": intent,
            "data": data
        }