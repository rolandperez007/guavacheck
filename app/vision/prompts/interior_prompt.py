class InteriorPromptBuilder:

    @staticmethod
    def build(project, room):

        return f"""
Create an ultra-realistic interior render.

Project Type:
{project.property_type}

Style:
{project.design_style}

Room:
{room.room_type}

Dimensions:
{room.width}m x {room.length}m

Budget:
{project.budget}

Lighting:
Natural daylight.

Architecture quality.

Luxury.

Photorealistic.

8K.
""".strip()