"""
OCR Pipeline Stage

Extracts text and metadata from uploaded
property documents.
"""


class OCRStage:

    name = "OCR"


    async def execute(
        self,
        context,
    ):


        documents = getattr(
            context,
            "documents",
            []
        )


        extracted_text = []


        result = {

            "completed": True,

            "text":
                extracted_text,

            "pages":
                0,

            "documents_processed":
                len(documents),

            "status":
                "PLACEHOLDER"

        }


        context.stages[
            self.name
        ] = result



        context.evidence.append(

            {

                "type":
                    "ocr_extraction",

                "data":
                    result

            }

        )


        return context