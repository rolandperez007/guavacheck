"""
Austin Context Builder

Builds the AI context before every response.

Sources

• Property Passport

• User

• Institution

• Workflow

• Community

• Notifications

• Finance

• Mortgage

• Currency

• Geo

• Vision

• Twin

• Session Memory

• Long-term Memory
"""

class ContextBuilder:

    def build(self, request):

        return {

            "user": request.get("user"),

            "passport": request.get("passport"),

            "institution": request.get("institution"),

            "workflow": request.get("workflow"),

            "community": request.get("community"),

            "finance": request.get("finance"),

            "geo": request.get("geo"),

            "currency": request.get("currency"),

            "memory": request.get("memory"),

            "vision": request.get("vision"),

            "twin": request.get("twin"),
        }