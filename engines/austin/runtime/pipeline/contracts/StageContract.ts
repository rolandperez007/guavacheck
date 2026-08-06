/**
 * =====================================================================
 * Austin Cognitive Operating System (ACOS)
 * ---------------------------------------------------------------------
 * StageContract
 *
 * Every execution stage within Austin must implement this contract.
 *
 * A stage performs exactly ONE responsibility inside the execution
 * pipeline.
 *
 * Examples:
 *  - ValidationStage
 *  - MemoryStage
 *  - KnowledgeStage
 *  - SimulationStage
 * =====================================================================
 */

import { PipelineContext } from "../PipelineContext";

export interface StageContract {
  /**
   * Unique stage identifier.
   */
  readonly name: string;

  /**
   * Determines whether this stage should execute.
   */
  canExecute(context: PipelineContext): Promise<boolean>;

  /**
   * Execute stage logic.
   */
  execute(context: PipelineContext): Promise<void>;

  /**
   * Roll back this stage if pipeline execution fails.
   */
  rollback?(context: PipelineContext): Promise<void>;
}
