export interface OrganizationVerification {
  organizationId: string;

  registrationVerified: boolean;

  addressVerified: boolean;

  directorsVerified: boolean;

  taxVerified: boolean;
}
