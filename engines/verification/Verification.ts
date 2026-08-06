export interface Verification {
  id: string;

  targetId: string;

  targetType: "user" | "organization" | "property" | "project" | "document" | "professional";

  status: "pending" | "in_review" | "verified" | "rejected" | "expired" | "suspended";

  trustScore: number;

  confidence: number;

  verifiedBy: string;

  verifiedAt?: Date;

  createdAt: Date;
}
