import { InvestorDeal, ROIChartPoint } from "./types";

export function toROIChart(data: InvestorDeal[]): ROIChartPoint[] {
  return data.map((deal) => ({
    label: deal.title,
    value: deal.roi,
  }));
}
