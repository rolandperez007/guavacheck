"""
GuavaCheck Finance Affordability Module

Buyer purchasing power intelligence.

Handles:
- income analysis
- affordability ratio
- buyer classification
- property budget estimation
"""

from typing import Dict, Any



class AffordabilityEngine:

    name = "affordability"



    def calculate(
        self,
        monthly_income: float,
        monthly_expenses: float,
        existing_debt: float = 0,
        savings: float = 0,
    ) -> Dict[str, Any]:
        """
        Calculates buyer affordability profile.
        """


        disposable_income = (
            monthly_income
            -
            monthly_expenses
            -
            existing_debt
        )


        if monthly_income <= 0:

            return {

                "status": "ERROR",

                "message": "Invalid income value",

            }



        affordability_ratio = (
            disposable_income
            /
            monthly_income
        ) * 100



        if affordability_ratio >= 60:

            profile = "STRONG"

        elif affordability_ratio >= 35:

            profile = "MODERATE"

        else:

            profile = "LIMITED"



        estimated_budget = (
            disposable_income
            *
            60
        )



        return {

            "status": "SUCCESS",

            "monthly_income": monthly_income,

            "monthly_expenses": monthly_expenses,

            "existing_debt": existing_debt,

            "savings": savings,

            "disposable_income": round(
                disposable_income,
                2,
            ),

            "affordability_ratio": round(
                affordability_ratio,
                2,
            ),

            "buyer_profile": profile,

            "estimated_property_budget": round(
                estimated_budget,
                2,
            ),

        }



    def compare_property(
        self,
        buyer_budget: float,
        property_price: float,
    ) -> Dict[str, Any]:
        """
        Compares buyer purchasing power
        against property asking price.
        """


        difference = (
            buyer_budget
            -
            property_price
        )


        if difference >= 0:

            decision = "AFFORDABLE"

        elif difference > (
            property_price * -0.25
        ):

            decision = "POSSIBLE_WITH_FINANCE"

        else:

            decision = "NOT_AFFORDABLE"



        return {

            "status": "SUCCESS",

            "buyer_budget": buyer_budget,

            "property_price": property_price,

            "difference": round(
                difference,
                2,
            ),

            "decision": decision,

        }