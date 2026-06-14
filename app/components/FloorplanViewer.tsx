"use client";

import { generateFloorplan } from "@/lib/floorplanEngine";

export default function FloorplanViewer({
  type,
  floors,
}: {
  type: "flat" | "duplex" | "terrace";
  floors: number;
}) {
  const plan = generateFloorplan({ type, floors });

  return (
    <div>
      <h3>Auto Floorplan</h3>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(4, 1fr)",
          gap: 10,
          marginTop: 10,
        }}
      >
        {plan.rooms.map((room, i) => (
          <div
            key={i}
            style={{
              border: "1px solid #ccc",
              padding: 10,
              borderRadius: 8,
              background: "#f9f9f9",
            }}
          >
            <b>{room.name}</b>
            <p>Floor: {room.floor}</p>
            <p>
              {room.width}m × {room.length}m
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}