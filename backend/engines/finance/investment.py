"""
GuavaCheck Finance Investment Module

Property investment intelligence layer.

Handles:
- ROI calculation
- rental yield analysis
- appreciation projections
- investment scoring
"""

from typing import Any


class InvestmentEngine:
    name = "investment"

    def calculate_roi(
        self,
        purchase_price: float,
        sale_price: float,
        additional_costs: float = 0,
    ) -> dict[str, Any]:
        """
        Calculates property investment return.
        """

        if purchase_price <= 0:
            return {
                "status": "ERROR",
                "message": "Invalid purchase price",
            }

        total_investment = purchase_price + additional_costs

        profit = sale_price - total_investment

        roi = (profit / total_investment) * 100

        return {
            "status": "SUCCESS",
            "purchase_price": purchase_price,
            "sale_price": sale_price,
            "profit": round(
                profit,
                2,
            ),
            "roi_percentage": round(
                roi,
                2,
            ),
        }

    def calculate_rental_yield(
        self,
        property_value: float,
        annual_rent: float,
    ) -> dict[str, Any]:
        """
        Calculates gross rental yield.
        """

        if property_value <= 0:
            return {
                "status": "ERROR",
                "message": "Invalid property value",
            }

        yield_percentage = (annual_rent / property_value) * 100

        return {
            "status": "SUCCESS",
            "property_value": property_value,
            "annual_rent": annual_rent,
            "rental_yield_percentage": round(
                yield_percentage,
                2,
            ),
        }

    def appreciation_projection(
        self,
        current_value: float,
        annual_growth_rate: float,
        years: int,
    ) -> dict[str, Any]:
        """
        Projects future property value.
        """

        future_value = current_value * (1 + annual_growth_rate / 100) ** years

        return {
            "status": "SUCCESS",
            "current_value": current_value,
            "growth_rate": annual_growth_rate,
            "years": years,
            "projected_value": round(
                future_value,
                2,
            ),
        }

    def investment_score(
        self,
        roi: float,
        rental_yield: float,
        risk_score: float,
    ) -> dict[str, Any]:
        """
        Basic investment intelligence score.

        Higher score indicates stronger
        investment characteristics.
        """

        score = (roi * 0.4) + (rental_yield * 0.4) + ((100 - risk_score) * 0.2)

        score = max(
            0,
            min(
                100,
                score,
            ),
        )

        return {
            "status": "SUCCESS",
            "investment_score": round(
                score,
                2,
            ),
            "classification": (
                "HIGH" if score >= 75 else "MEDIUM" if score >= 50 else "LOW"
            ),
        }
