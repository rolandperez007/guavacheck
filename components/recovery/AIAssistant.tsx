"use client";

import { useEffect, useState } from "react";

export default function AIAssistant() {
  const messages = [
    "System alert: page not found…",
    "Activating Guava recovery protocol…",
    "Scanning property network…",
    "Recommended routes are ready."
  ];

  const [index, setIndex] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setIndex((prev) => (prev + 1) % messages.length);
    }, 2500);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="text-center text-white text-lg font-light">
      🤖 {messages[index]}
    </div>
  );
}


