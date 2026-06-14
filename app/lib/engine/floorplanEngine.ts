// lib/engine/floorplanEngine.ts

export type FloorplanInput = {
  type: "flat" | "duplex" | "terrace";
  floors: number;
  landSize?: number; // sqm
};

export type Room = {
  name: string;
  width: number;
  length: number;
};

export type FloorplanOutput = {
  floors: {
    floor: number;
    rooms: Room[];
  }[];
};

export function generateFloorplan(input: FloorplanInput): FloorplanOutput {
  const landSize = input.landSize || 400;

  const baseRooms = {
    flat: [
      { name: "Living Room", size: 40 },
      { name: "Kitchen", size: 18 },
      { name: "Master Bedroom", size: 30 },
      { name: "Bedroom 2", size: 20 },
      { name: "Bathroom", size: 10 },
    ],

    duplex: [
      { name: "Living Room", size: 45 },
      { name: "Kitchen", size: 20 },
      { name: "Dining", size: 18 },
      { name: "Guest Room", size: 22 },
      { name: "Staircase Core", size: 15 },
    ],

    terrace: [
      { name: "Living Room", size: 35 },
      { name: "Kitchen", size: 15 },
      { name: "Bedroom", size: 25 },
      { name: "Bathroom", size: 10 },
    ],
  };

  const layout = baseRooms[input.type];

  const floors: FloorplanOutput["floors"] = [];

  for (let i = 0; i < input.floors; i++) {
    floors.push({
      floor: i + 1,
      rooms: layout.map((r) => ({
        name: r.name,
        width: Math.sqrt(r.size * (landSize / 100)),
        length: Math.sqrt(r.size * (landSize / 100)),
      })),
    });
  }

  return { floors };
}