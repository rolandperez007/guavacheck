export class IntentClassifier {

  async parse(input: string) {
    const text = input.toLowerCase();

    // Default structure
    const base = {
      raw: input,
      confidence: 0,
      entities: {},
      type: "unknown"
    };

    // 🧱 BOQ / construction cost
    if (
      text.includes("boq") ||
      text.includes("build") ||
      text.includes("construction") ||
      text.includes("cost") ||
      text.includes("duplex") ||
      text.includes("house")
    ) {
      return {
        ...base,
        type: "boq_analysis",
        confidence: 0.9
      };
    }

    // 🏠 Property valuation
    if (
      text.includes("worth") ||
      text.includes("value") ||
      text.includes("valuation") ||
      text.includes("price of")
    ) {
      return {
        ...base,
        type: "property_valuation",
        confidence: 0.88
      };
    }

    // 🧑‍🔧 Contractor verification
    if (
      text.includes("contractor") ||
      text.includes("builder") ||
      text.includes("engineer") ||
      text.includes("trust") ||
      text.includes("verify")
    ) {
      return {
        ...base,
        type: "contractor_verification",
        confidence: 0.85
      };
    }

    // 📈 ROI / investment
    if (
      text.includes("roi") ||
      text.includes("return") ||
      text.includes("investment") ||
      text.includes("rent") ||
      text.includes("yield")
    ) {
      return {
        ...base,
        type: "investment_analysis",
        confidence: 0.87
      };
    }

    // 💰 Mortgage / affordability
    if (
      text.includes("mortgage") ||
      text.includes("loan") ||
      text.includes("afford") ||
      text.includes("payment")
    ) {
      return {
        ...base,
        type: "mortgage_analysis",
        confidence: 0.86
      };
    }

    // 🏘 Property search
    if (
      text.includes("buy") ||
      text.includes("rent") ||
      text.includes("property") ||
      text.includes("apartment") ||
      text.includes("house in")
    ) {
      return {
        ...base,
        type: "property_search",
        confidence: 0.82
      };
    }

    // ⚠ Fraud / risk
    if (
      text.includes("scam") ||
      text.includes("fraud") ||
      text.includes("fake") ||
      text.includes("safe") ||
      text.includes("risk")
    ) {
      return {
        ...base,
        type: "risk_analysis",
        confidence: 0.9
      };
    }

    return base;
  }
}
