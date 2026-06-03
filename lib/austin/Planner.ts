export class Planner {

  async create(intent: any) {

    const type = intent?.type;

    switch (type) {

      // 🧱 BOQ / Construction Planning
      case "boq_analysis":
        return {
          intent: type,
          steps: [
            "fetch_material_prices",
            "fetch_labor_rates",
            "apply_location_multiplier",
            "calculate_total_cost",
            "generate_boq_table",
            "store_result"
          ],
          output: "table"
        };

      // 🏠 Property valuation
      case "property_valuation":
        return {
          intent: type,
          steps: [
            "fetch_property_data",
            "fetch_comparable_properties",
            "calculate_market_value",
            "adjust_for_location",
            "generate_valuation_report",
            "store_result"
          ],
          output: "insight"
        };

      // 🧑‍🔧 Contractor verification
      case "contractor_verification":
        return {
          intent: type,
          steps: [
            "fetch_contractor_profile",
            "check_previous_projects",
            "analyze_reviews_and_risk",
            "compute_trust_score",
            "generate_verification_report",
            "store_result"
          ],
          output: "report"
        };

      // 📈 Investment / ROI
      case "investment_analysis":
        return {
          intent: type,
          steps: [
            "fetch_rental_data",
            "estimate_rental_income",
            "calculate_roi",
            "compare_market_yield",
            "generate_investment_score",
            "store_result"
          ],
          output: "scorecard"
        };

      // 💰 Mortgage
      case "mortgage_analysis":
        return {
          intent: type,
          steps: [
            "fetch_interest_rates",
            "calculate_monthly_payment",
            "estimate_affordability",
            "generate_payment_schedule",
            "store_result"
          ],
          output: "finance_table"
        };

      // 🏘 Property search
      case "property_search":
        return {
          intent: type,
          steps: [
            "query_property_database",
            "filter_by_budget_and_location",
            "rank_by_value",
            "generate_listing_cards"
          ],
          output: "listings"
        };

      // ⚠ Risk / fraud
      case "risk_analysis":
        return {
          intent: type,
          steps: [
            "analyze_user_input",
            "check_fraud_patterns",
            "evaluate_risk_score",
            "generate_risk_warning"
          ],
          output: "risk_report"
        };

      // 🧠 fallback
      default:
        return {
          intent: "unknown",
          steps: [
            "log_request",
            "return_general_response"
          ],
          output: "message"
        };
    }
  }
}
