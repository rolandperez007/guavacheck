"use client";

import { Canvas } from "@react-three/fiber";
import { OrbitControls, Box } from "@react-three/drei";
import { mapPropertyToModel } from "@/lib/architectureEngine";

export default function Property3DViewer({
  property,
}: {
  property: any;
}) {
  const modelConfig = mapPropertyToModel(property);

  const model = [];

  const baseHeight = 0.2;

  // 🧱 BASE
  model.push({
    type: "base",
    position: [0, 0, 0],
    scale: [modelConfig.width, baseHeight, modelConfig.length],
  });

  // 🏢 FLOORS
  for (let i = 0; i < modelConfig.floors; i++) {
    model.push({
      type: "floor",
      position: [0, baseHeight + i * 1.2, 0],
      scale: [modelConfig.width, 1, modelConfig.length],
    });
  }

  return (
    <div style={{ height: 450, width: "100%" }}>
      <Canvas camera={{ position: [5, 5, 5] }}>
        <ambientLight intensity={0.6} />
        <directionalLight position={[5, 10, 5]} intensity={1} />

        {model.map((part, i) => (
          <Box key={i} position={part.position} args={part.scale}>
            <meshStandardMaterial
              color={part.type === "base" ? "#666" : "#9ecbff"}
            />
          </Box>
        ))}

        <OrbitControls />
      </Canvas>
    </div>
  );
}