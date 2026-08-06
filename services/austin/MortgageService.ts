import { ConstructionPricingModel } from "@/lib/austin/models/ConstructionPricingModel";

export class MortgageService {
  static calculatePayment(input: {
    price: number;
    downPaymentPercent?: number;
    interestRate?: number;
    years?: number;
  }) {
    const downPaymentPercent = input.downPaymentPercent || 20;
    const interestRate = input.interestRate || 10;
    const years = input.years || 20;

    const principal = input.price * (1 - downPaymentPercent / 100);

    const monthlyRate = interestRate / 100 / 12;
    const months = years * 12;

    const monthly = (principal * monthlyRate) / (1 - Math.pow(1 + monthlyRate, -months));

    return {
      principal,
      monthly: Math.round(monthly),
      totalPayment: Math.round(monthly * months),
      meta: {
        model: "mortgage-engine-v1",
      },
    };
  }
}
