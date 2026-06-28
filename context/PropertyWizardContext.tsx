"use client";

import {
  createContext,
  useContext,
  useState,
  ReactNode,
} from "react";

import {
  PropertyWizardData,
  WizardStep,
} from "@/types/PropertyWizard";

interface PropertyWizardContextType {
  wizard: PropertyWizardData;

  setWizard: React.Dispatch<
    React.SetStateAction<PropertyWizardData>
  >;

  updateWizard: (
    data: Partial<PropertyWizardData>
  ) => void;

  goToStep: (step: WizardStep) => void;

  resetWizard: () => void;
}

const defaultWizard: PropertyWizardData = {
  intent: null,

  property: {
    name: "",
    propertyType: "",

    bedrooms: 0,
    bathrooms: 0,
    toilets: 0,

    parkingSpaces: 0,

    landSize: 0,
    buildingSize: 0,

    floors: 1,

    yearBuilt: undefined,

    condition: "",

    furnished: false,

    description: "",
  },

  location: {
    country: "",
    state: "",
    city: "",

    area: "",

    street: "",

    postalCode: "",

    latitude: undefined,
    longitude: undefined,

    landmark: "",
  },

  media: {
    photos: [],
    videos: [],
    floorPlans: [],
    droneImages: [],
    virtualTours: [],
  },

  documents: {
    certificateOfOccupancy: [],
    surveyPlan: [],
    deedOfAssignment: [],
    buildingApproval: [],
    taxClearance: [],
    valuationReport: [],
    otherDocuments: [],
  },

  ai: {
    estimatedValue: undefined,
    suggestedPrice: undefined,
    confidence: undefined,

    recommendations: [],
    warnings: [],
    strengths: [],
  },

  services: {
    verification: false,
    agentAssignment: false,
    legalReview: false,
    valuation: false,
    photography: false,
    dronePhotography: false,
    premiumPromotion: false,
    buildingPassport: false,
  },

  progress: {
    currentStep: "welcome",
    completedSteps: [],
    percentage: 0,
    isComplete: false,
  },
};

const PropertyWizardContext =
  createContext<PropertyWizardContextType | undefined>(
    undefined
  );

export function PropertyWizardProvider({
  children,
}: {
  children: ReactNode;
}) {
  const [wizard, setWizard] =
    useState<PropertyWizardData>(defaultWizard);

  function updateWizard(
    data: Partial<PropertyWizardData>
  ) {
    setWizard((prev) => ({
      ...prev,
      ...data,
    }));
  }

  function goToStep(step: WizardStep) {
    setWizard((prev) => ({
      ...prev,
      progress: {
        ...prev.progress,
        currentStep: step,
      },
    }));
  }

  function resetWizard() {
    setWizard(defaultWizard);
  }

  return (
    <PropertyWizardContext.Provider
      value={{
        wizard,
        setWizard,
        updateWizard,
        goToStep,
        resetWizard,
      }}
    >
      {children}
    </PropertyWizardContext.Provider>
  );
}

export function usePropertyWizardContext() {
  const context = useContext(PropertyWizardContext);

  if (!context) {
    throw new Error(
      "usePropertyWizardContext must be used inside PropertyWizardProvider"
    );
  }

  return context;
}