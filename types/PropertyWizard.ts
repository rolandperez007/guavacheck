/**
 * ============================================
 * guavacheck Property Wizard
 * Master Type Definitions
 * ============================================
 */

export type WizardIntent =
  | "sell"
  | "distress"
  | "rent"
  | "build"
  | "commercial"
  | "design"
  | "estimate";

export type WizardStep =
  | "welcome"
  | "intent"
  | "property"
  | "location"
  | "media"
  | "documents"
  | "austin"
  | "services"
  | "review"
  | "complete";

export interface PropertyInformation {
  name: string;
  propertyType: string;

  bedrooms: number;
  bathrooms: number;
  toilets: number;

  parkingSpaces: number;

  landSize: number;
  buildingSize: number;

  floors: number;

  yearBuilt?: number;

  condition: string;

  furnished: boolean;

  description: string;
}

export interface PropertyLocation {
  country: string;
  state: string;
  city: string;

  area: string;

  street: string;

  postalCode?: string;

  latitude?: number;
  longitude?: number;

  landmark?: string;
}

export interface PropertyMedia {
  photos: File[];

  videos: File[];

  floorPlans: File[];

  droneImages: File[];

  virtualTours: File[];
}

export interface PropertyDocuments {
  certificateOfOccupancy: File[];

  surveyPlan: File[];

  deedOfAssignment: File[];

  buildingApproval: File[];

  taxClearance: File[];

  valuationReport: File[];

  otherDocuments: File[];
}

export interface AustinAnalysis {
  estimatedValue?: number;

  suggestedPrice?: number;

  confidence?: number;

  recommendations: string[];

  warnings: string[];

  strengths: string[];
}

export interface SelectedServices {
  verification: boolean;

  agentAssignment: boolean;

  legalReview: boolean;

  valuation: boolean;

  photography: boolean;

  dronePhotography: boolean;

  premiumPromotion: boolean;

  buildingPassport: boolean;
}

export interface WizardProgress {
  currentStep: WizardStep;

  completedSteps: WizardStep[];

  percentage: number;

  isComplete: boolean;
}

export interface PropertyWizardData {
  intent: WizardIntent | null;

  property: PropertyInformation;

  location: PropertyLocation;

  media: PropertyMedia;

  documents: PropertyDocuments;

  ai: AustinAnalysis;

  services: SelectedServices;

  progress: WizardProgress;
}