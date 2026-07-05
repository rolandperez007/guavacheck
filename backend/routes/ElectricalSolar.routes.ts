// backend/routes/ElectricalSolar.routes.ts

import { Router } from "express";
import { ElectricalSolarController } from "../controllers/ElectricalSolar.controller";

const router = Router();

/**
 * Base Route:
 * /api/v1/electrical-solar
 */

// Health Check
router.get(
  "/health",
  ElectricalSolarController.health
);

// Validate Input
router.post(
  "/validate",
  ElectricalSolarController.validateInput
);

// Quick System Estimate
router.post(
  "/estimate",
  ElectricalSolarController.estimate
);

// Full Engineering Design & Report
router.post(
  "/design",
  ElectricalSolarController.generateDesign
);

export default router;