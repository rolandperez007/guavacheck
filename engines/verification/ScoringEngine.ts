import { RuleResult } from "./RuleEngine";

export interface VerificationScore {
  total: number;

  confidence: number;

  passed: number;

  failed: number;
}

export class ScoringEngine {
  static calculate(results: RuleResult[]): VerificationScore {
    const passed = results.filter((r) => r.passed).length;

    const failed = results.length - passed;

    const total = results.reduce((sum, r) => sum + r.score, 0);

    return {
      total,

      confidence: results.length === 0 ? 0 : total / results.length,

      passed,

      failed,
    };
  }
}
