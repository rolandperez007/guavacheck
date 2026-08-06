export interface VerificationCheck {
  entityId: string;

  nextReview: Date;

  frequencyDays: number;
}

export class ContinuousVerification {
  static due(check: VerificationCheck): boolean {
    return new Date() >= check.nextReview;
  }
}
