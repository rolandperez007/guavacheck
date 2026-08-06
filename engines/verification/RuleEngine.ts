export interface VerificationRule {
  id: string;

  name: string;

  description: string;

  weight: number;

  enabled: boolean;
}

export interface RuleResult {
  ruleId: string;

  passed: boolean;

  score: number;

  reason: string;
}

export class RuleEngine {
  static evaluate(
    rules: VerificationRule[],
    evaluator: (rule: VerificationRule) => RuleResult,
  ): RuleResult[] {
    return rules.map(evaluator);
  }
}
