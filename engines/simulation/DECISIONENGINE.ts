export interface Decision {
  id: string;

  reason: string;

  confidence: number;

  approved: boolean;
}

export class DecisionEngine {
  static approve(confidence: number): boolean {
    return confidence >= 95;
  }
}
