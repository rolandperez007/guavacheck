/**
 * GuavaCheck AI System
 * Project Orchestrator
 * ----------------------------
 * This is the master execution layer.
 *
 * It coordinates:
 * - Engineering Engine (civil, structural, etc.)
 * - AI Layer (design, cost, blueprint)
 * - Final unified project output
 */

import { EngineeringEngine } from "../core/EngineeringEngine";
import { EngineeringRegistry } from "../core/EngineeringRegistry";

// Engineering modules
import { CivilEngineering } from "../modules/civil/CivilEngineering";
import { StructuralAnalysis } from "../modules/structural/StructuralAnalysis";
import { ElectricalEngineering } from "../modules/electrical/ElectricalEngineering";
import { MechanicalEngineering } from "../modules/mechanical/MechanicalEngineering";
import { PlumbingEngineering } from "../modules/plumbing/PlumbingEngineering";
import { HVACEngineering } from "../modules/hvac/HVACEngineering";
import { FireSafetyEngineering } from "../modules/fire/FireSafetyEngineering";

// AI layer
import { CostEstimationEngine } from "../ai/CostEstimationEngine";
import { DesignGenerator } from "../ai/DesignGenerator";
import { BlueprintCompiler } from "../ai/BlueprintCompiler";

export interface ProjectInput {
  context: any;

  civil?: any;
  structural?: any;
  electrical?: any;
  mechanical?: any;
  plumbing?: any;
  hvac?: any;
  fire?: any;
}

export interface FullProjectOutput {
  engineering: Record<string, any>;
  design: any;
  cost: any;
  blueprint: any;
}

export class ProjectOrchestrator {
  private registry: EngineeringRegistry;
  private engine: EngineeringEngine;

  constructor() {
    this.registry = new EngineeringRegistry();
    this.engine = new EngineeringEngine(this.registry);

    this.registerModules();
  }

  /**
   * Register all engineering modules
   */
  private registerModules() {
    this.registry.register(new CivilEngineering());
    this.registry.register(new StructuralAnalysis());
    this.registry.register(new ElectricalEngineering());
    this.registry.register(new MechanicalEngineering());
    this.registry.register(new PlumbingEngineering());
    this.registry.register(new HVACEngineering());
    this.registry.register(new FireSafetyEngineering());
  }

  /**
   * Run full engineering + AI pipeline
   */
  async runFullProject(input: ProjectInput): Promise<FullProjectOutput> {
    // ======================================================
    // 1. ENGINEERING LAYER EXECUTION
    // ======================================================

    const engineeringResults: Record<string, any> = {};

    const run = async (discipline: string, data: any) => {
      if (!data) return null;

      return await this.engine.run({
        discipline: discipline as any,
        context: input.context,
        data,
      });
    };

    engineeringResults.civil = await run("civil", input.civil);
    engineeringResults.structural = await run("structural", input.structural);
    engineeringResults.electrical = await run("electrical", input.electrical);
    engineeringResults.mechanical = await run("mechanical", input.mechanical);
    engineeringResults.plumbing = await run("plumbing", input.plumbing);
    engineeringResults.hvac = await run("hvac", input.hvac);
    engineeringResults.fire = await run("fire_safety", input.fire);

    // ======================================================
    // 2. AI DESIGN GENERATION
    // ======================================================

    const design = DesignGenerator.generate({
      buildingType: input.context.buildingType || "residential",
      areaSqm: input.context.areaSqm || 100,
      floors: input.context.floors || 1,
      style: input.context.style || "modern",
    });

    // ======================================================
    // 3. COST ESTIMATION
    // ======================================================

    const cost = CostEstimationEngine.estimate({
      areaSqm: input.context.areaSqm || 100,
      floors: input.context.floors || 1,
      region: input.context.location?.country || "GLOBAL",
      qualityLevel: input.context.quality || "standard",
    });

    // ======================================================
    // 4. BLUEPRINT COMPILATION
    // ======================================================

    const blueprint = BlueprintCompiler.compile({
      design,
      cost,
      engineeringSummary: engineeringResults,
    });

    // ======================================================
    // 5. FINAL OUTPUT
    // ======================================================

    return {
      engineering: engineeringResults,
      design,
      cost,
      blueprint,
    };
  }
}
