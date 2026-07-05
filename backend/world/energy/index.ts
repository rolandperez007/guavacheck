// backend/world/energy/index.ts

/**
 * Guava World Energy Intelligence
 *
 * This module provides region-aware energy intelligence for every
 * engineering engine in the platform.
 *
 * Consumers:
 * - ElectricalSolar.engine.ts
 * - Gene Smart Home
 * - Digital Twin
 * - Energy Cost Estimator
 * - Carbon Calculator
 * - Future AI Planning Modules
 */

export interface EnergyEnvironment {
  regionId: string;

  country: string;
  state?: string;
  city?: string;

  climateZone: string;

  averageSunHours: number;

  solarEfficiencyFactor: number;

  systemLossFactor: number;

  gridReliability: number;

  electricityTariff: number;

  preferredSystem:
    | "grid-tied"
    | "off-grid"
    | "hybrid";

  preferredBattery:
    | "lifepo4"
    | "lithium-ion"
    | "lead-acid";

  voltageStandard: number;

  frequencyHz: number;

  notes: string[];
}

/**
 * Default environment
 */
const DEFAULT_ENVIRONMENT: EnergyEnvironment = {
  regionId: "GLOBAL",

  country: "Global",

  climateZone: "temperate",

  averageSunHours: 5,

  solarEfficiencyFactor: 0.85,

  systemLossFactor: 0.20,

  gridReliability: 0.70,

  electricityTariff: 0.15,

  preferredSystem: "hybrid",

  preferredBattery: "lifepo4",

  voltageStandard: 230,

  frequencyHz: 50,

  notes: [
    "Default global engineering assumptions."
  ]
};

/**
 * Initial regional intelligence.
 * This will later be populated automatically
 * from your world dataset.
 */
const REGIONS: Record<string, Partial<EnergyEnvironment>> = {

  NG: {
    country: "Nigeria",
    climateZone: "tropical",

    averageSunHours: 5.5,

    solarEfficiencyFactor: 0.84,

    systemLossFactor: 0.20,

    gridReliability: 0.45,

    preferredSystem: "hybrid",

    preferredBattery: "lifepo4",

    voltageStandard: 230,

    frequencyHz: 50,

    notes: [
      "Frequent grid interruptions.",
      "Solar + battery strongly recommended."
    ]
  },

  US: {
    country: "United States",

    climateZone: "mixed",

    averageSunHours: 5.2,

    solarEfficiencyFactor: 0.88,

    systemLossFactor: 0.15,

    gridReliability: 0.98,

    preferredSystem: "grid-tied",

    preferredBattery: "lifepo4",

    voltageStandard: 120,

    frequencyHz: 60
  },

  DE: {
    country: "Germany",

    climateZone: "continental",

    averageSunHours: 3.4,

    solarEfficiencyFactor: 0.90,

    systemLossFactor: 0.15,

    gridReliability: 0.99,

    preferredSystem: "grid-tied",

    preferredBattery: "lifepo4",

    voltageStandard: 230,

    frequencyHz: 50
  }

};

/**
 * Returns engineering environment
 * for a supplied region/country code.
 */
export function getEnergyEnvironment(
  regionCode?: string
): EnergyEnvironment {

  if (!regionCode) {
    return DEFAULT_ENVIRONMENT;
  }

  return {
    ...DEFAULT_ENVIRONMENT,
    ...(REGIONS[regionCode.toUpperCase()] || {})
  };
}