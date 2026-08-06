"use client";

import { useEffect, useRef, useState } from "react";
import { generateFloorplan } from "@/lib/floorplanEngine";

export default function FloorplanViewer({
  type,
  floors,
}: {
  type: "flat" | "duplex" | "terrace";
  floors: number;
}) {
  const plan = generateFloorplan({ type, floors });
  const svgRef = useRef<HTMLDivElement>(null);
  const [selectedRoom, setSelectedRoom] = useState<any>(null);

  useEffect(() => {
    const container = svgRef.current;
    if (!container) return;

    const handleClick = (e: any) => {
      const target = e.target;

      const roomId = target?.getAttribute?.("data-room-id");
      if (!roomId) return;

      const room = plan.rooms.find((r) => r.id === roomId);
      if (room) {
        setSelectedRoom(room);
      }
    };

    container.addEventListener("click", handleClick);

    return () => container.removeEventListener("click", handleClick);
  }, [plan]);

  return (
    <div style={{ display: "flex", gap: 20 }}>
      {/* SVG VIEW */}
      <div>
        <h3>Auto Floorplan</h3>

        <div
          ref={svgRef}
          style={{
            marginTop: 10,
            border: "1px solid #ddd",
            borderRadius: 8,
            padding: 10,
            background: "#fff",
            overflow: "auto",
            cursor: "pointer",
          }}
          dangerouslySetInnerHTML={{ __html: plan.svg }}
        />
      </div>

      {/* INSPECTOR PANEL */}
      <div
        style={{
          width: 250,
          padding: 10,
          border: "1px solid #ddd",
          borderRadius: 8,
          background: "#fafafa",
        }}
      >
        <h4>Room Inspector</h4>

        {selectedRoom ? (
          <div>
            <p>
              <b>Name:</b> {selectedRoom.name}
            </p>
            <p>
              <b>Floor:</b> {selectedRoom.floor}
            </p>
            <p>
              <b>Width:</b> {selectedRoom.width.toFixed(2)}m
            </p>
            <p>
              <b>Length:</b> {selectedRoom.length.toFixed(2)}m
            </p>
          </div>
        ) : (
          <p>Click a room to view details</p>
        )}
      </div>
    </div>
  );
}
