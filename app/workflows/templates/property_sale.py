from .base_template import BaseWorkflowTemplate


class PropertySaleTemplate(
    BaseWorkflowTemplate,
):

    name = "property_sale"

    category = "property"

    description = "Property sale workflow."

    def build(self):

        return [
            "passport.verify",
            "document.generate",
            "billing.invoice",
            "notification.send",
        ]