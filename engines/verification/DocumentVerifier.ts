export interface DocumentVerification {
  documentId: string;

  verified: boolean;

  confidence: number;

  reviewer?: string;

  reviewedAt?: Date;
}
