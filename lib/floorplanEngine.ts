type Room = {
  id: string;
  name: string;
  floor: number;
  width: number;
  length: number;
};

export function generateFloorplan({
  type,
  floors,
}: {
  type: "flat" | "duplex" | "terrace";
  floors: number;
}) {
  const rooms: Room[] = [];

  const baseRooms =
    type === "flat"
      ? ["Living Room", "Bedroom", "Kitchen", "Bathroom"]
      : type === "duplex"
      ? ["Living Room", "Kitchen", "Master Bedroom", "Bedroom", "Bathroom"]
      : ["Living Room", "Kitchen", "Bedroom", "Bedroom", "Bathroom"];

  let id = 1;

  for (let f = 1; f <= floors; f++) {
    baseRooms.forEach((name) => {
      rooms.push({
        id: `room-${id++}`,
        name,
        floor: f,
        width: 4 + Math.random() * 2,
        length: 4 + Math.random() * 3,
      });
    });
  }

  const svgRooms = rooms
    .map((r, i) => {
      const x = (i % 4) * 120;
      const y = Math.floor(i / 4) * 120;

      return `
        <rect x="${x}" y="${y}" width="100" height="100" fill="#e8f4ff" stroke="#333"/>
        <text x="${x + 10}" y="${y + 50}" font-size="10">${r.name}</text>
      `;
    })
    .join("");

  const svg = `
    <svg width="700" height="450" xmlns="http://www.w3.org/2000/svg">
      ${svgRooms}
    </svg>
  `;

  return {
    rooms,
    svg,
  };
}