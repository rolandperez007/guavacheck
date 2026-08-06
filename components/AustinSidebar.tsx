"use client";

import { useEffect, useState } from "react";

export default function AustinSidebar() {
  const [ws, setWs] = useState<WebSocket | null>(null);
  const [messages, setMessages] = useState<any[]>([]);
  const [input, setInput] = useState("");

  useEffect(() => {
    const socket = new WebSocket("ws://127.0.0.1:8000/ws/austin");

    socket.onopen = () => {
      console.log("Austin WS connected");
    };

    socket.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        setMessages((prev) => [...prev, data]);
      } catch (e) {
        console.log("Invalid WS message", e);
      }
    };

    socket.onerror = (err) => {
      console.log("WS error", err);
    };

    setWs(socket);

    return () => socket.close();
  }, []);

  const sendQuery = async () => {
    if (!ws) return;

    // WebSocket (real-time channel)
    ws.send(
      JSON.stringify({
        query: input,
        user_id: "frontend-user",
      }),
    );

    // HTTP fallback (backend API)
    try {
      const res = await fetch("http://127.0.0.1:8000/austin/execute", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          query: input,
          user_id: "frontend-user",
        }),
      });

      const data = await res.json();

      setMessages((prev) => [
        ...prev,
        {
          type: "api_response",
          data,
        },
      ]);
    } catch (err) {
      console.log("API error", err);
    }

    setInput("");
  };

  return (
    <div style={{ width: 400, height: "100vh", background: "#000", color: "#fff", padding: 10 }}>
      <h3>Austin AI</h3>

      <div style={{ height: "85%", overflowY: "auto", border: "1px solid #333", padding: 10 }}>
        {messages.map((m, i) => (
          <pre key={i} style={{ fontSize: 12 }}>
            {JSON.stringify(m, null, 2)}
          </pre>
        ))}
      </div>

      <input
        style={{ width: "100%", marginTop: 10 }}
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Ask Austin..."
      />

      <button style={{ width: "100%", marginTop: 5 }} onClick={sendQuery}>
        Send
      </button>
    </div>
  );
}
