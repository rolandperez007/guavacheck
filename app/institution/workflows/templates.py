class InstitutionWorkflowTemplateService:
    """
    Institution-specific workflow templates.
    """

    def available_templates(
        self,
    ):
        return [
            "property_verification",
            "mortgage_approval",
            "tenant_screening",
            "institution_onboarding",
            "property_transfer",
        ]