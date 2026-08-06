export interface ProfessionalVerification {
  professionalId: string;

  profession: string;

  licenseVerified: boolean;

  organizationVerified: boolean;

  trustScore: number;
}
