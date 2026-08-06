from .base_template import BaseWorkflowTemplate


class PropertyPurchaseTemplate(
    BaseWorkflowTemplate,
):

    name = "property_purchase"

    category = "property"

    description = "Purchase workflow."

    def build(self):

        return [
            "passport.verify",
            "billing.invoice",
            "document.generate",
            "notification.send",
        ]