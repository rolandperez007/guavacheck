export interface VerificationReport {
  id: string;

  generatedAt: Date;

  verified: number;

  pending: number;

  rejected: number;

  suspended: number;
}
