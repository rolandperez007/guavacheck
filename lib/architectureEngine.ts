export type PropertyType = "flat" | "duplex" | "terrace";

export type PropertyInput = {
  type: PropertyType;
  floors: number;
  width: number;
  length: number;
};

export type ModelPart = {
  type: "base" | "floor" | "roof";
  position: [number, number, number];
  scale: [number, number, number];
};

export function generateBuildingModel(input: PropertyInput): ModelPart[] {
  const { type, floors, width, length } = input;

  const model: ModelPart[] = [];

  const baseHeight = 0.2;

  // 🧱 BASE FOUNDATION
  model.push({
    type: "base",
    position: [0, 0, 0],
    scale: [width, baseHeight, length],
  });

  // 🏢 FLOORS
  for (let i = 0; i < floors; i++) {
    model.push({
      type: "floor",
      position: [0, baseHeight + i * 1.2, 0],
      scale: [width * (type === "terrace" ? 1 : 0.9), 1, length * (type === "terrace" ? 1 : 0.9)],
    });
  }

  // 🏠 ROOF
  model.push({
    type: "roof",
    position: [0, baseHeight + floors * 1.2, 0],
    scale: [width, 0.3, length],
  });

  return model;
}

/**
 * Compatibility alias for frontend usage
 */
export function mapPropertyToModel(input: PropertyInput): ModelPart[] {
  return generateBuildingModel(input);
}
