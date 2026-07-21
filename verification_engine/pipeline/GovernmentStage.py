"""
Government Verification Stage

Connects government intelligence services
into the verification pipeline.
"""

from verification_engine.government.intelligence import (
    GovernmentIntelligenceService,
)


class GovernmentStage:

    name = "GOVERNMENT"


    def __init__(self):

        self.service = GovernmentIntelligenceService()



    async def execute(
        self,
        context,
    ):

        property_data = getattr(
            context,
            "property_data",
            {}
        )


        country = property_data.get(
            "country",
            "NG"
        )


        documents = getattr(
            context,
            "documents",
            []
        )


        compliance = (
            self.service
            .verify_document_requirements(
                country,
                documents
            )
        )


        sources = (
            self.service
            .find_verification_sources(
                "verify_land_title"
            )
        )


        context.government_result = {

            "country": country,

            "compliance": compliance,

            "sources": sources,

            "status": "INTELLIGENCE_READY"

        }


        context.evidence.append(

            {

                "type": "government",

                "data": context.government_result

            }

        )


        return context