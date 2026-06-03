export class ROIService {

  static calculateROI(
    investment: number,
    annualIncome: number
  ) {

    if (!investment) return 0;

    return (
      annualIncome /
      investment
    ) * 100;
  }
}
