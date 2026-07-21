"""
Certificate Stage

Prepares verification certificate
data for certificate generation.
"""


from datetime import datetime
import uuid



class CertificateStage:

    name = "CERTIFICATE"



    async def execute(
        self,
        context,
    ):


        trust_score = getattr(
            context,
            "trust_score",
            0
        )


        trust_data = (
            context.stages
            .get(
                "TRUST",
                {}
            )
        )


        approved = (
            trust_score >= 75
        )


        certificate_id = None


        if approved:

            certificate_id = (
                "GVC-"
                +
                str(
                    uuid.uuid4()
                )
                .upper()
                [:12]
            )



        certificate = {

            "certificate_ready":
                approved,

            "certificate_id":
                certificate_id,

            "qr_ready":
                approved,

            "issued_at":
                datetime.utcnow()
                .isoformat(),

            "verification_level":
                trust_data.get(
                    "trust_level",
                    "UNKNOWN"
                ),

            "trust_score":
                trust_score,

            "property_id":
                context.property_id,

            "status":
                "READY"
                if approved
                else "REVIEW_REQUIRED"

        }



        context.certificate = certificate


        context.stages[
            self.name
        ] = certificate



        context.evidence.append(

            {

                "type":
                    "verification_certificate",

                "data":
                    certificate

            }

        )


        return context