"use client";

import { useEffect, useMemo, useState } from "react";

interface EventItem {
  id: number;
  source: string;
  message: string;
  timestamp: string;
}

export default function LiveEventFeed() {
  const [events, setEvents] = useState<EventItem[]>([
    {
      id: 1,
      source: "Austin",
      message: "Verification demand increased in Lagos and queue pressure is rising.",
      timestamp: "just now",
    },
  ]);

  useEffect(() => {
    const handler = (event: MessageEvent) => {
      try {
        const payload = JSON.parse(event.data);
        if (payload?.type === "austin-event") {
          setEvents((current) => [
            {
              id: Date.now(),
              source: payload.source || "Austin",
              message: payload.message || "Live platform update",
              timestamp: "now",
            },
            ...current,
          ].slice(0, 8));
        }
      } catch {
        // ignore malformed frames
      }
    };

    const socket = new WebSocket("ws://127.0.0.1:8000/ws/austin");
    socket.addEventListener("message", handler);

    return () => {
      socket.removeEventListener("message", handler);
      socket.close();
    };
  }, []);

  const content = useMemo(() => events, [events]);

  return (
    <section className="rounded-2xl border border-slate-800 bg-slate-950/90 p-6">
      <div>
        <p className="text-sm uppercase tracking-[0.35em] text-slate-500">Live activity feed</p>
        <h3 className="mt-2 text-xl font-semibold text-white">Austin is monitoring live platform events</h3>
      </div>

      <div className="mt-5 space-y-3">
        {content.map((item) => (
          <div key={item.id} className="rounded-xl border border-slate-800 bg-slate-900/80 p-4 text-sm text-slate-300">
            <div className="flex items-center justify-between gap-3">
              <div className="font-semibold text-white">{item.source}</div>
              <div className="text-xs uppercase tracking-[0.25em] text-slate-500">{item.timestamp}</div>
            </div>
            <div className="mt-2">{item.message}</div>
          </div>
        ))}
      </div>
    </section>
  );
}
