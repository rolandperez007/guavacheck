"use client";

import { useState } from "react";

export function useAustinStream() {
  const [events, setEvents] = useState<any[]>([]);
  const [finalData, setFinalData] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  async function run(input: string) {
    setEvents([]);
    setFinalData(null);
    setLoading(true);

    const res = await fetch("/api/austin/execute", {
      method: "POST",
      body: JSON.stringify({ input }),
    });

    const reader = res.body?.getReader();
    const decoder = new TextDecoder();

    if (!reader) return;

    while (true) {
      const { value, done } = await reader.read();
      if (done) break;

      const chunk = decoder.decode(value);
      const lines = chunk.split("\n\n");

      for (const line of lines) {
        if (!line.trim()) continue;

        try {
          const json = JSON.parse(line.replace("data: ", ""));
          setEvents((prev) => [...prev, json]);

          if (json.stage === "complete") {
            setFinalData(json.data);
          }
        } catch (e) {}
      }
    }

    setLoading(false);
  }

  return { run, events, finalData, loading };
}
