export interface TrustProfile {
  entityId: string;

  score: number;

  level: string;

  lastUpdated: Date;
}

export class TrustEngine {
  static calculate(score: number): string {
    if (score >= 95) return "Elite";

    if (score >= 85) return "Trusted";

    if (score >= 70) return "Verified";

    return "Unverified";
  }
}
