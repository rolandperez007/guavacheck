"use client";

import { useState } from "react";
import { useAustinStream } from "@/hooks/useAustinStream";
import { AustinRenderer } from "./AustinRenderer";
import { AustinTimeline } from "./AustinTimeline";

export default function AustinChat() {
  const [input, setInput] = useState("");

  const { run, events, finalData, loading } = useAustinStream();

  const handleSend = async () => {
    if (!input.trim()) return;
    await run(input);
    setInput("");
  };

  return (
    <div className="min-h-screen bg-gray-50 flex justify-center">
      
      <div className="w-full max-w-3xl p-6 space-y-6">

        {/* HEADER */}
        <div className="text-center space-y-1">
          <h1 className="text-2xl font-semibold tracking-tight">
            Austin Intelligence
          </h1>
          <p className="text-sm text-gray-500">
            Property • Construction • Investment Analysis Engine
          </p>
        </div>

        {/* INPUT CARD */}
        <div className="bg-white border rounded-xl shadow-sm p-3 flex gap-2">
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask Austin about construction, valuation, ROI..."
            className="flex-1 outline-none text-sm"
          />

          <button
            onClick={handleSend}
            className="bg-black text-white text-sm px-4 py-2 rounded-lg hover:opacity-90 transition"
          >
            {loading ? "Thinking..." : "Ask"}
          </button>
        </div>

        {/* TIMELINE */}
        {events?.length > 0 && (
          <div className="animate-fadeIn">
            <AustinTimeline events={events} />
          </div>
        )}

        {/* DEBUG FEED (SOFT + MINIMAL) */}
        {events?.length > 0 && (
          <div className="bg-white border rounded-lg p-3 text-xs text-gray-500 space-y-1">
            {events.map((e, i) => (
              <div key={i} className="flex gap-2">
                <span className="font-medium text-gray-700">
                  {e.stage}
                </span>
                <span>{e.step ? `→ ${e.step}` : ""}</span>
              </div>
            ))}
          </div>
        )}

        {/* FINAL OUTPUT */}
        {finalData && (
          <div className="animate-fadeIn">
            <AustinRenderer data={finalData} />
          </div>
        )}

      </div>
    </div>
  );
}