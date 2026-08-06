/**
 * GuavaCheck Engineering Engine
 * Engineering Calculator Core (Upgraded)
 * ---------------------------------------
 * This is the mathematical backbone of the entire system.
 *
 * It provides:
 * - Structural mechanics helpers
 * - Electrical load modeling
 * - Civil/environmental estimation
 * - Unit conversions
 * - Safety factors
 * - Physics-style utility functions
 *
 * This file is intentionally dependency-light so all modules
 * can rely on it without circular coupling.
 */

export class EngineeringCalculator {
  // =========================================================
  // 📐 UNIT CONVERSIONS
  // =========================================================

  static sqmToSqft(value: number): number {
    return value * 10.7639;
  }

  static sqftToSqm(value: number): number {
    return value / 10.7639;
  }

  static kwToWatts(kw: number): number {
    return kw * 1000;
  }

  static wattsToKw(watts: number): number {
    return watts / 1000;
  }

  static mmToMeters(mm: number): number {
    return mm / 1000;
  }

  static metersToMm(m: number): number {
    return m * 1000;
  }

  // =========================================================
  // 🏗 STRUCTURAL ENGINEERING CORE
  // =========================================================

  /**
   * Simply distributed load per unit length
   */
  static distributeLoad(totalLoad: number, length: number): number {
    if (length <= 0) throw new Error("Invalid structural length");
    return totalLoad / length;
  }

  /**
   * Bending moment (simply supported beam approximation)
   * M = (W × L) / 8
   */
  static bendingMoment(totalLoad: number, span: number): number {
    return (totalLoad * span) / 8;
  }

  /**
   * Stress calculation
   * σ = M / Z
   */
  static bendingStress(moment: number, sectionModulus: number): number {
    if (sectionModulus <= 0) {
      throw new Error("Invalid section modulus");
    }
    return moment / sectionModulus;
  }

  /**
   * Deflection estimation (simplified beam model)
   */
  static beamDeflection(load: number, span: number, elasticity: number): number {
    if (elasticity <= 0) throw new Error("Invalid elasticity modulus");

    return (load * Math.pow(span, 3)) / (48 * elasticity);
  }

  // =========================================================
  // ⚡ ELECTRICAL ENGINEERING CORE
  // =========================================================

  /**
   * Residential electrical load estimation
   */
  static estimateElectricalLoad(areaSqm: number, loadFactor = 30): number {
    if (areaSqm <= 0) throw new Error("Invalid area");
    return areaSqm * loadFactor; // Watts
  }

  /**
   * Voltage-current relationship
   * P = V × I
   */
  static currentFromPower(powerWatts: number, voltage: number): number {
    if (voltage <= 0) throw new Error("Invalid voltage");
    return powerWatts / voltage;
  }

  /**
   * Generator sizing with safety margin
   */
  static generatorSize(loadKw: number, margin = 1.25): number {
    return loadKw * margin;
  }

  // =========================================================
  // 🌬 HVAC / THERMAL CORE
  // =========================================================

  /**
   * Cooling load (very simplified BTU model)
   */
  static estimateCoolingLoad(areaSqm: number, height = 3): number {
    const volume = areaSqm * height;
    return volume * 50; // BTU approximation
  }

  /**
   * Air change rate estimate (ACH)
   */
  static airChangeRate(volume: number, airflow: number): number {
    if (volume <= 0) throw new Error("Invalid volume");
    return airflow / volume;
  }

  // =========================================================
  // 🚰 CIVIL / FLUID CORE
  // =========================================================

  /**
   * Rainfall runoff estimation (basic civil model)
   */
  static runoffVolume(area: number, rainfallMm: number): number {
    return area * (rainfallMm / 1000);
  }

  /**
   * Pipe flow estimation (simplified)
   */
  static pipeFlowRate(diameterMm: number, pressure: number): number {
    if (diameterMm <= 0) throw new Error("Invalid diameter");
    return Math.sqrt(diameterMm) * pressure * 0.1;
  }

  // =========================================================
  // 🛡 SAFETY / ENGINEERING FACTORS
  // =========================================================

  /**
   * Apply safety factor
   */
  static applySafetyFactor(value: number, factor: number): number {
    if (factor <= 0) throw new Error("Invalid safety factor");
    return value * factor;
  }

  /**
   * Factor of safety check
   */
  static factorOfSafety(breakingStrength: number, appliedLoad: number): number {
    if (appliedLoad <= 0) throw new Error("Invalid load");
    return breakingStrength / appliedLoad;
  }

  /**
   * Safe/unsafe evaluation helper
   */
  static isSafe(factorOfSafety: number, threshold = 1.5): boolean {
    return factorOfSafety >= threshold;
  }

  // =========================================================
  // 📊 GENERAL ENGINEERING HELPERS
  // =========================================================

  static percentage(part: number, total: number): number {
    if (total === 0) throw new Error("Invalid total");
    return (part / total) * 100;
  }

  static clamp(value: number, min: number, max: number): number {
    return Math.max(min, Math.min(max, value));
  }

  static average(values: number[]): number {
    if (!values.length) throw new Error("Empty dataset");
    return values.reduce((a, b) => a + b, 0) / values.length;
  }
}
