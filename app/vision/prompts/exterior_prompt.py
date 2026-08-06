class ExteriorPromptBuilder:
    @staticmethod
    def build(project):

        return f"""
Create an ultra-realistic exterior render.

Property Type:
{project.property_type}

Style:
{project.design_style}

Budget:
{project.budget}

Luxury architecture.

Professional architectural visualization.

8K.
""".strip()
