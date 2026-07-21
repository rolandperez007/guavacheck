"""
Fraud Detection Stage

Detects suspicious activity,
duplicate ownership,
forged documents,
and identity anomalies.
"""


class FraudStage:

    name = "FRAUD"


    async def execute(
        self,
        context,
    ):


        alerts = []

        risk_score = 0


        registry_result = (
            context.stages
            .get(
                "REGISTRY",
                {}
            )
        )


        document_result = (
            context.stages
            .get(
                "DOCUMENT",
                {}
            )
        )


        government_result = (
            context.stages
            .get(
                "GOVERNMENT",
                {}
            )
        )


        #
        # Basic fraud indicators
        #


        if not document_result.get(
            "documents_valid",
            False
        ):

            alerts.append(
                "Document validation incomplete"
            )

            risk_score += 10



        if government_result.get(
            "status"
        ) != "INTELLIGENCE_READY":

            alerts.append(
                "Government intelligence unavailable"
            )

            risk_score += 10



        registry = (
            registry_result
            .get(
                "registry",
                {}
            )
        )


        if registry.get(
            "overall_status"
        ) == "DISPUTED":

            alerts.append(
                "Registry dispute detected"
            )

            risk_score += 40



        fraud_result = {

            "completed": True,

            "fraud_detected":
                risk_score >= 50,

            "risk_score":
                risk_score,

            "alerts":
                alerts,

            "status":
                "ANALYZED"

        }


        context.stages[
            self.name
        ] = fraud_result



        context.evidence.append(

            {

                "type":
                    "fraud_analysis",

                "data":
                    fraud_result

            }

        )


        return context