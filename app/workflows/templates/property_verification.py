from .base_template import BaseWorkflowTemplate


class PropertyVerificationTemplate(
    BaseWorkflowTemplate,
):

    name = "property_verification"

    category = "property"

    description = (
        "Complete property verification workflow."
    )

    def build(self):

        return [
            "passport.verify",
            "vision.analyze",
            "decision.evaluate",
            "institution.validate",
            "document.generate",
            "notification.send",
        ]