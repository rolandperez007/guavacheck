import { useEffect, useState } from "react";

export function useAustinStream() {
  const [event, setEvent] = useState<any>(null);

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8000/ws/austin");

    ws.onmessage = (msg) => {
      try {
        const data = JSON.parse(msg.data);
        setEvent(data);
      } catch (e) {
        console.error("Invalid WS event:", e);
      }
    };

    ws.onerror = (err) => {
      console.error("WebSocket error:", err);
    };

    return () => ws.close();
  }, []);

  return event;
}
