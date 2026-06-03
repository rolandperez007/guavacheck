export type PropertyType = "flat" | "duplex" | "terrace";

export type FloorplanRoom = {
  name: string;
  width: number;
  length: number;
  floor: number;
  position: [number, number, number];
};

export type FloorplanResult = {
  floors: number;
  rooms: FloorplanRoom[];
};

export function generateFloorplan(input: {
  type: PropertyType;
  floors: number;
}) : FloorplanResult {
  const { type, floors } = input;

  const rooms: FloorplanRoom[] = [];

  const baseRooms = [
    { name: "Living Room", w: 4, l: 5 },
    { name: "Kitchen", w: 3, l: 3 },
    { name: "Bathroom", w: 2, l: 2 },
  ];

  const bedroom = type === "flat" ? 1 : type === "duplex" ? 3 : 4;

  for (let floor = 0; floor < floors; floor++) {
    let offsetX = 0;

    // 🏠 Bedrooms
    for (let i = 0; i < bedroom; i++) {
      rooms.push({
        name: `Bedroom ${i + 1}`,
        width: 3,
        length: 3,
        floor,
        position: [offsetX, floor * 3, 0],
      });

      offsetX += 3.5;
    }

    // 🧱 Common rooms (only ground floor)
    if (floor === 0) {
      baseRooms.forEach((r, i) => {
        rooms.push({
          name: r.name,
          width: r.w,
          length: r.l,
          floor,
          position: [i * 4, 0, 5],
        });
      });
    }
  }

  return {
    floors,
    rooms,
  };
}