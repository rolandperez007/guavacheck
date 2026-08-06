class FloorplanPromptBuilder:
    @staticmethod
    def build(project):

        return f"""
Generate a professional architectural floor plan.

Property:
{project.property_type}

Style:
{project.design_style}

Budget:
{project.budget}

Include dimensions.

Black and white.

Architectural drawing.
""".strip()
