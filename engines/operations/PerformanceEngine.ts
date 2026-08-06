export interface PerformanceMetric {
  name: string;
  value: number;
  unit: string;
  timestamp: Date;
}

export class PerformanceEngine {
  private static metrics: PerformanceMetric[] = [];

  static record(metric: PerformanceMetric): void {
    this.metrics.push(metric);
  }

  static latest(name: string): PerformanceMetric | undefined {
    return [...this.metrics].reverse().find((m) => m.name === name);
  }

  static all(): PerformanceMetric[] {
    return this.metrics;
  }
}
