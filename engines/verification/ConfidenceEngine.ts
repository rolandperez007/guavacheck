export interface ConfidenceFactor {
  name: string;

  weight: number;

  score: number;
}

export class ConfidenceEngine {
  static calculate(factors: ConfidenceFactor[]): number {
    if (factors.length === 0) return 0;

    const weighted = factors.reduce(
      (sum, factor) => sum + factor.weight * factor.score,

      0,
    );

    const totalWeight = factors.reduce(
      (sum, factor) => sum + factor.weight,

      0,
    );

    return totalWeight === 0 ? 0 : weighted / totalWeight;
  }
}
