"use client";

import { useEffect, useRef } from "react";

type Event = {
  stage: string;
  step?: string;
  status?: string;
  data?: any;
};

export function AustinTimeline({ events }: { events: Event[] }) {
  const endRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [events]);

  return (
    <div
      style={{
        maxHeight: 220,
        overflowY: "auto",
        border: "1px solid #eee",
        borderRadius: 12,
        padding: 12,
        background: "#fafafa",
        fontFamily: "monospace",
        fontSize: 12
      }}
    >
      {events.map((e, i) => (
        <div key={i} style={{ marginBottom: 6 }}>
          <span style={{ fontWeight: 600 }}>{e.stage}</span>
          {e.step && <span> → {e.step}</span>}
          {e.status && <span> ({e.status})</span>}
        </div>
      ))}
      <div ref={endRef} />
    </div>
  );
}









