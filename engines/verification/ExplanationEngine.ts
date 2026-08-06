export interface VerificationExplanation {
  decision: string;

  confidence: number;

  reasons: string[];

  recommendations: string[];
}

export class ExplanationEngine {
  static generate(
    decision: string,

    confidence: number,

    reasons: string[],

    recommendations: string[],
  ): VerificationExplanation {
    return {
      decision,

      confidence,

      reasons,

      recommendations,
    };
  }
}
