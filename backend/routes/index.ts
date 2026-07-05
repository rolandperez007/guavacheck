// backend/routes/index.ts

import { Router } from "express";

import electricalSolarRoutes from "./ElectricalSolar.routes";

const router = Router();

/**
 * API Version 1
 * Base: /api/v1
 */

// Electrical + Solar Engineering
router.use(
  "/electrical-solar",
  electricalSolarRoutes
);

export default router;