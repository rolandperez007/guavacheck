/**
 * =====================================================================
 * PipelineContract
 *
 * Defines the responsibilities of every Austin execution pipeline.
 *
 * A pipeline is responsible for coordinating the execution of all
 * registered stages.
 * =====================================================================
 */

import { PipelineRequest } from "../PipelineRequest";
import { PipelineResponse } from "../PipelineResponse";
import { StageContract } from "./StageContract";

export interface PipelineContract {
  /**
   * Register a stage.
   */
  registerStage(stage: StageContract): void;

  /**
   * Remove a stage.
   */
  unregisterStage(stageName: string): void;

  /**
   * Execute the complete pipeline.
   */
  execute(request: PipelineRequest): Promise<PipelineResponse>;
}
