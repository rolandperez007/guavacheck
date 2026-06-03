export class ReportService {

  static generateConstructionReport(input: any, boq: any) {

    const sqm = input?.sqm || 400;
    const level = input?.level || "standard";
    const location = input?.location || "default";

    const phases = [
      { phase: "Foundation", durationWeeks: 3, cost: boq.breakdown.foundation },
      { phase: "Structure", durationWeeks: 6, cost: boq.breakdown.structure },
      { phase: "Roofing", durationWeeks: 3, cost: boq.breakdown.roofing },
      { phase: "Finishing", durationWeeks: 5, cost: boq.breakdown.finishing },
      { phase: "External Works", durationWeeks: 2, cost: boq.breakdown.externalWorks }
    ];

    const totalWeeks = phases.reduce((a, p) => a + p.durationWeeks, 0);

    return {
      title: "Austin Construction Report",
      project: { sqm, level, location },
      summary: {
        totalCost: boq.total,
        durationWeeks: totalWeeks,
        costPerSqm: Math.round(boq.total / sqm)
      },
      phases,
      insights: [
        Project type: ,
        Location: ,
        Estimated duration:  weeks
      ],
      risk: boq.confidence < 0.75 ? "HIGH" : "MEDIUM",
      export: { format: ["pdf-ready", "json"] }
    };
  }
}
