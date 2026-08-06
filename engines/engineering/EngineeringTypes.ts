/**
 * GuavaCheck Engineering Engine
 * Core Type Definitions
 * ----------------------------
 * This file defines the foundational contracts used across all engineering modules:
 * Civil, Structural, Electrical, HVAC, Plumbing, etc.
 */

export type CountryCode = "NG" | "US" | "UK" | "CA" | "AE" | "GLOBAL";

export type EngineeringDiscipline =
  "civil" | "structural" | "electrical" | "mechanical" | "plumbing" | "hvac" | "fire_safety";

export type UnitSystem = "metric" | "imperial";

export interface GeoLocation {
  country: CountryCode;
  state?: string;
  city?: string;
  coordinates?: {
    lat: number;
    lng: number;
  };
}

export interface ProjectContext {
  id: string;
  name: string;

  location: GeoLocation;

  unitSystem: UnitSystem;

  currency: string;

  /**
   * Land / building scale inputs
   */
  plotArea?: number; // m²
  buildingFootprint?: number; // m²
  floors?: number;

  /**
   * Optional AI enhancement context
   */
  aiContext?: Record<string, any>;

  createdAt: Date;
  updatedAt: Date;
}

/**
 * Generic engineering input payload
 */
export interface EngineeringInput<T = any> {
  discipline: EngineeringDiscipline;
  context: ProjectContext;
  data: T;
}

/**
 * Standard engineering output format
 */
export interface EngineeringResult<T = any> {
  discipline: EngineeringDiscipline;

  success: boolean;

  summary: string;

  data: T;

  metrics?: Record<string, number>;

  warnings?: string[];

  errors?: string[];

  generatedAt: Date;
}

/**
 * Every module MUST implement this interface
 */
export interface IEngineeringModule<TInput = any, TOutput = any> {
  discipline: EngineeringDiscipline;

  validate(input: EngineeringInput<TInput>): Promise<void>;

  compute(input: EngineeringInput<TInput>): Promise<EngineeringResult<TOutput>>;
}

/**
 * Registry entry wrapper
 */
export interface RegisteredModule {
  discipline: EngineeringDiscipline;
  module: IEngineeringModule;
  version: string;
}
