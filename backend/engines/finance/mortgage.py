"""
GuavaCheck Finance Mortgage Module

Property lending intelligence layer.

Handles:
- mortgage repayment estimates
- interest calculations
- loan projections
- affordability preparation
"""


from typing import Dict, Any

import math



class MortgageEngine:

    name = "mortgage"



    def calculate_payment(
        self,
        principal: float,
        annual_interest_rate: float,
        years: int,
    ) -> Dict[str, Any]:
        """
        Calculate monthly mortgage repayment.

        Formula:
        M = P(r(1+r)^n)/((1+r)^n-1)
        """

        if years <= 0:

            return {

                "status": "ERROR",

                "message": "Invalid loan duration",

            }


        monthly_rate = (
            annual_interest_rate / 100
        ) / 12


        months = years * 12


        if monthly_rate == 0:

            payment = principal / months

        else:

            payment = (
                principal
                *
                (
                    monthly_rate
                    *
                    math.pow(
                        1 + monthly_rate,
                        months,
                    )
                )
                /
                (
                    math.pow(
                        1 + monthly_rate,
                        months,
                    )
                    -
                    1
                )
            )


        total_payment = payment * months


        return {

            "status": "SUCCESS",

            "principal": principal,

            "annual_interest_rate": annual_interest_rate,

            "years": years,

            "monthly_payment": round(
                payment,
                2,
            ),

            "total_payment": round(
                total_payment,
                2,
            ),

            "interest_paid": round(
                total_payment - principal,
                2,
            ),

        }



    def estimate_affordable_property(
        self,
        monthly_income: float,
        debt_ratio: float = 0.35,
        years: int = 20,
        annual_interest_rate: float = 10,
    ) -> Dict[str, Any]:
        """
        Estimates purchasing power based on income.
        """

        affordable_payment = (
            monthly_income * debt_ratio
        )


        monthly_rate = (
            annual_interest_rate / 100
        ) / 12


        months = years * 12


        if monthly_rate == 0:

            loan = affordable_payment * months

        else:

            loan = (
                affordable_payment
                *
                (
                    (
                        math.pow(
                            1 + monthly_rate,
                            months,
                        )
                        -
                        1
                    )
                    /
                    (
                        monthly_rate
                        *
                        math.pow(
                            1 + monthly_rate,
                            months,
                        )
                    )
                )
            )


        return {

            "status": "SUCCESS",

            "monthly_income": monthly_income,

            "estimated_property_budget": round(
                loan,
                2,
            ),

            "assumed_debt_ratio": debt_ratio,

            "years": years,

        }