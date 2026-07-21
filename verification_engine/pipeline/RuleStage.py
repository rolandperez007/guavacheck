"""
Rule Stage

Executes business validation rules.

Evaluates collected evidence and applies
verification decision rules.
"""


class RuleStage:

    name = "RULE_ENGINE"


    async def execute(
        self,
        context,
    ):


        rules_checked = 0

        rules_passed = 0

        rules_failed = 0


        #
        # Evidence sources
        #

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


        registry_result = (
            context.stages
            .get(
                "REGISTRY",
                {}
            )
        )


        fraud_result = (
            context.stages
            .get(
                "FRAUD",
                {}
            )
        )



        #
        # Rule: Documents exist
        #

        rules_checked += 1

        if document_result.get(
            "documents_received",
            0
        ) > 0:

            rules_passed += 1

        else:

            rules_failed += 1



        #
        # Rule: Government intelligence available
        #

        rules_checked += 1

        if government_result.get(
            "status"
        ) == "INTELLIGENCE_READY":

            rules_passed += 1

        else:

            rules_failed += 1



        #
        # Rule: Fraud risk acceptable
        #

        rules_checked += 1

        if fraud_result.get(
            "risk_score",
            100
        ) < 50:

            rules_passed += 1

        else:

            rules_failed += 1



        #
        # Rule: Registry response exists
        #

        rules_checked += 1

        if registry_result:

            rules_passed += 1

        else:

            rules_failed += 1



        rule_result = {

            "completed": True,

            "rules_checked":
                rules_checked,

            "rules_passed":
                rules_passed,

            "rules_failed":
                rules_failed,

            "verification_ready":
                rules_failed == 0,

            "status":
                "EVALUATED"

        }



        context.stages[
            self.name
        ] = rule_result



        context.evidence.append(

            {

                "type":
                    "business_rules",

                "data":
                    rule_result

            }

        )


        return context