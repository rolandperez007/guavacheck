export interface InvestorDeal {
  id: string;
  title: string;
  roi: number;
  investmentScore: number;
  distressedScore: number;
}

export interface ROIChartPoint {
  label: string;
  value: number;
}