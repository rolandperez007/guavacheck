from .base_template import BaseWorkflowTemplate


class MortgageApprovalTemplate(
    BaseWorkflowTemplate,
):

    name = "mortgage_approval"

    category = "finance"

    description = (
        "Mortgage approval workflow."
    )

    def build(self):

        return [
            "passport.verify",
            "institution.validate",
            "simulation.run",
            "decision.evaluate",
            "billing.invoice",
            "notification.send",
        ]