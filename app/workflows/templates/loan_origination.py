from .base_template import BaseWorkflowTemplate


class LoanOriginationTemplate(
    BaseWorkflowTemplate,
):

    name = "loan_origination"

    category = "finance"

    description = "Loan processing."

    def build(self):

        return [
            "institution.validate",
            "simulation.run",
            "decision.evaluate",
        ]