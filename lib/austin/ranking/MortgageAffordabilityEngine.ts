export interface MortgageInput {
  propertyPrice: number;
  downPaymentPercent?: number; // default 20%
  annualInterestRate?: number; // default 18%
  years?: number; // default 20
  monthlyIncome?: number;
}

export class MortgageAffordabilityEngine {
  static calculate(input: MortgageInput) {
    const price = input.propertyPrice;

    const downPaymentRate = (input.downPaymentPercent ?? 20) / 100;
    const interestRate = (input.annualInterestRate ?? 18) / 100;
    const years = input.years ?? 20;

    const principal = price * (1 - downPaymentRate);
    const monthlyRate = interestRate / 12;
    const months = years * 12;

    const monthlyPayment = (principal * monthlyRate) / (1 - Math.pow(1 + monthlyRate, -months));

    const totalPayment = monthlyPayment * months;
    const totalInterest = totalPayment - principal;

    // affordability logic
    const income = input.monthlyIncome ?? monthlyPayment * 3;
    const affordabilityRatio = monthlyPayment / income;

    let status: "SAFE" | "STRETCHED" | "RISKY" = "SAFE";

    if (affordabilityRatio > 0.6) status = "RISKY";
    else if (affordabilityRatio > 0.4) status = "STRETCHED";

    return {
      propertyPrice: price,
      principal: Math.round(principal),
      monthlyPayment: Math.round(monthlyPayment),
      totalPayment: Math.round(totalPayment),
      totalInterest: Math.round(totalInterest),

      affordabilityRatio: Number(affordabilityRatio.toFixed(2)),
      status,

      recommendation: status === "SAFE" ? "BUY" : status === "STRETCHED" ? "CAUTION" : "AVOID",
    };
  }
}
