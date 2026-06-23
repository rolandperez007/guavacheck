export class LearningLoop {

  static memory: any[] = [];

  static record(event: any) {

    this.memory.push({
      ...event,
      timestamp: new Date()
    });

    return { stored: true, total: this.memory.length };
  }

  static analyzePerformance() {

    const total = this.memory.length;

    const successfulDeals = this.memory.filter(m => m.outcome === "SUCCESS").length;
    const failedDeals = this.memory.filter(m => m.outcome === "FAIL").length;

    const successRate = total > 0 ? (successfulDeals / total) * 100 : 0;

    return {
      totalEvents: total,
      successRate: Math.round(successRate),
      trend: successRate > 60 ? "IMPROVING" : "DECLINING"
    };
  }

  static suggestImprovements() {

    const analysis = this.analyzePerformance();

    const suggestions: string[] = [];

    if (analysis.successRate < 50) {
      suggestions.push("Increase negotiation aggressiveness");
      suggestions.push("Improve property valuation weighting");
    }

    if (analysis.successRate > 70) {
      suggestions.push("Scale autonomous listings");
      suggestions.push("Increase deal auto-approval rate");
    }

    return {
      analysis,
      suggestions
    };
  }
}

