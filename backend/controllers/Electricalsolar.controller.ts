// backend/controllers/ElectricalSolar.controller.ts

import { Request, Response, NextFunction } from "express";
import { ElectricalSolarService } from "../services/ElectricalSolar.service";

export class ElectricalSolarController {
  /**
   * Generate complete electrical + solar engineering report
   * POST /api/v1/electrical-solar/design
   */
  static async generateDesign(req: Request, res: Response, next: NextFunction) {
    try {
      const result = await ElectricalSolarService.processSolarRequest(req.body);

      if (result.status === "error") {
        return res.status(400).json(result);
      }

      return res.status(200).json({
        success: true,
        module: "ElectricalSolar",
        timestamp: new Date().toISOString(),
        ...result,
      });
    } catch (error) {
      next(error);
    }
  }

  /**
   * Validate submitted engineering payload
   * POST /api/v1/electrical-solar/validate
   */
  static async validateInput(req: Request, res: Response, next: NextFunction) {
    try {
      const payload = req.body;

      // Schema validation will later be delegated to AJV/Zod
      const valid = payload && payload.projectId && payload.location && payload.loadProfile;

      if (!valid) {
        return res.status(400).json({
          success: false,
          message: "Invalid electrical/solar payload.",
        });
      }

      return res.status(200).json({
        success: true,
        message: "Payload validation passed.",
      });
    } catch (error) {
      next(error);
    }
  }

  /**
   * Quick sizing endpoint
   * POST /api/v1/electrical-solar/estimate
   */
  static async estimate(req: Request, res: Response, next: NextFunction) {
    try {
      const result = await ElectricalSolarService.processSolarRequest(req.body);

      return res.status(200).json({
        success: true,
        sizing: result.data?.sizing,
        flags: result.data?.flags,
      });
    } catch (error) {
      next(error);
    }
  }

  /**
   * Health check
   * GET /api/v1/electrical-solar/health
   */
  static async health(req: Request, res: Response) {
    return res.status(200).json({
      success: true,
      module: "ElectricalSolar",
      status: "online",
      version: "1.0.0",
      timestamp: new Date().toISOString(),
    });
  }
}
