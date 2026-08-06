export interface VerificationEvent {
  id: string;

  entityId: string;

  event: string;

  actor: string;

  createdAt: Date;
}
