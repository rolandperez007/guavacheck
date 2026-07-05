// ElectricalSolar.engine.ts

type SystemType = "grid-tied" | "off-grid" | "hybrid";

interface ElectricalSolarInput {
  projectId: string;
  systemType: SystemType;

  location: {
    country: string;
    state?: string;
    city: string;
    sunHoursPerDay?: number;
    regionId?: string;
  };

  loadProfile: {
    totalLoadKW: number;
    peakLoadKW?: number;
    dailyConsumptionKWh: number;
  };

  solarArray: {
    panelWattage: number;
    numberOfPanels?: number;
  };

  batterySystem: {
    batteryType: string;
    capacityKWh?: number;
    autonomyDays?: number;
  };

  inverterSystem: {
    capacityKW?: number;
    efficiencyPercent?: number;
  };
}

/**
 * Simulated world environment lookup (you already said this exists in /world)
 */
function getWorldEnvironment(location: any) {
  // In real system, this pulls from /world/geo, climate, grid stability, etc.
  return {
    sunHoursPerDay: location.sunHoursPerDay || 5,
    systemLossFactor: 0.2, // 20% loss default for Africa-style environments
    gridStability: location.country === "Nigeria" ? "unstable" : "stable",
    solarEfficiencyMultiplier: 0.85
  };
}

/**
 * Core Engine
 */
export function computeElectricalSolarSystem(input: ElectricalSolarInput) {
  const env = getWorldEnvironment(input.location);

  const sunHours = env.sunHoursPerDay;
  const lossFactor = env.systemLossFactor;

  // -----------------------------
  // 1. Energy Core Calculations
  // -----------------------------
  const dailyEnergy = input.loadProfile.dailyConsumptionKWh;

  const usableSolarPerKW = sunHours * (1 - lossFactor) * env.solarEfficiencyMultiplier;

  const requiredSolarKW = dailyEnergy / usableSolarPerKW;

  const panelWatt = input.solarArray.panelWattage;
  const requiredPanels = Math.ceil((requiredSolarKW * 1000) / panelWatt);

  // -----------------------------
  // 2. Battery Sizing Logic
  // -----------------------------
  const autonomyDays = input.batterySystem.autonomyDays || 1.5;

  const requiredBatteryKWh = dailyEnergy * autonomyDays * (1 + lossFactor);

  // -----------------------------
  // 3. Inverter Sizing Logic
  // -----------------------------
  const inverterEfficiency = input.inverterSystem.efficiencyPercent
    ? input.inverterSystem.efficiencyPercent / 100
    : 0.9;

  const requiredInverterKW = input.loadProfile.peakLoadKW
    ? input.loadProfile.peakLoadKW / inverterEfficiency
    : input.loadProfile.totalLoadKW / inverterEfficiency;

  // -----------------------------
  // 4. Auto-sizing Adjustment Layer (lightweight)
  // -----------------------------
  const autoAdjustments: string[] = [];

  let finalBattery = input.batterySystem.capacityKWh;
  if (!finalBattery || finalBattery < requiredBatteryKWh) {
    finalBattery = requiredBatteryKWh;
    autoAdjustments.push("Battery size auto-adjusted to meet autonomy requirement");
  }

  let finalInverter = input.inverterSystem.capacityKW;
  if (!finalInverter || finalInverter < requiredInverterKW) {
    finalInverter = requiredInverterKW;
    autoAdjustments.push("Inverter upgraded to match peak load demand");
  }

  // -----------------------------
  // 5. Engineering Report Output (B)
  // -----------------------------
  const engineeringReport = {
    projectId: input.projectId,
    environment: env,

    energyAnalysis: {
      dailyConsumptionKWh: dailyEnergy,
      usableSolarPerKWPerDay: usableSolarPerKW,
      requiredSolarKW
    },

    solarDesign: {
      panelWattage: panelWatt,
      requiredPanels,
      totalSolarKW: (requiredPanels * panelWatt) / 1000
    },

    batteryDesign: {
      requiredBatteryKWh,
      selectedBatteryKWh: finalBattery,
      autonomyDays
    },

    inverterDesign: {
      requiredInverterKW,
      selectedInverterKW: finalInverter
    },

    systemSummary: {
      systemType: input.systemType,
      efficiencyLoss: lossFactor,
      gridStatus: env.gridStability,
      autoAdjustments
    }
  };

  // -----------------------------
  // 6. API-Ready Output (A)
  // -----------------------------
  const apiResponse = {
    projectId: input.projectId,
    status: "computed",

    sizing: {
      solarKW: requiredSolarKW,
      panels: requiredPanels,
      batteryKWh: finalBattery,
      inverterKW: finalInverter
    },

    flags: {
      autoAdjusted: autoAdjustments.length > 0,
      warnings: autoAdjustments
    }
  };

  return {
    engineeringReport,
    apiResponse
  };
}