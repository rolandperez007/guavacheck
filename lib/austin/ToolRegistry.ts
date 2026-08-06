export const ToolRegistry = {
  boq: {
    calculateTotalCost: (data: any) => ({ total: 0, breakdown: [] }),
    generateTable: (data: any) => ({ rows: [] }),
  },

  valuation: {
    generateReport: (data: any) => ({ report: "ok" }),
  },
};
