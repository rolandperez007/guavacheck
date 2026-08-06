"""
Austin Suggestion Engine

Produces proactive suggestions while the user is browsing.

Examples

• Better mortgage

• Nearby schools

• Better pricing

• Similar properties

• Investment advice

• Insurance

• Legal verification

• Builder recommendations

• Interior ideas

• Community insights
"""


class SuggestionEngine:

    def generate(self, context):

        suggestions = []

        if context.get("passport"):

            suggestions.append("Run complete verification")

            suggestions.append("Estimate renovation cost")

            suggestions.append("Compare nearby sales")

        return suggestions