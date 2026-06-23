"use client"
"use client";

import { Canvas } from "@react-three/fiber";
import { OrbitControls, Box } from "@react-three/drei";
import { mapPropertyToModel, ModelPart } from "@/lib/architectureEngine";

export default function Property3DViewer({ property }: { property: any }) {
  const model: ModelPart[] = mapPropertyToModel(property);

  return (
    <div style={{ height: 450, width: "100%" }}>
      <Canvas camera={{ position: [5, 5, 5] }}>
        <ambientLight intensity={0.6} />
        <directionalLight position={[5, 10, 5]} intensity={1} />

        {model.map((part, i) => {
          const color =
            part.type === "base"
              ? "#666666"
              : part.type === "roof"
              ? "#444444"
              : "#9ecbff";

          return (
            <Box key={i} position={part.position as any} args={part.scale as any}>
              <meshStandardMaterial color={color} />
            </Box>
          );
        })}

        <OrbitControls />
      </Canvas>
    </div>
  );
}