export interface ValidationSource {
  source: string;

  verified: boolean;

  confidence: number;
}

export class CrossValidationEngine {
  static validate(sources: ValidationSource[]): boolean {
    return sources.every((source) => source.verified);
  }

  static confidence(sources: ValidationSource[]): number {
    if (sources.length === 0) return 0;

    return (
      sources.reduce(
        (sum, source) => sum + source.confidence,

        0,
      ) / sources.length
    );
  }
}
