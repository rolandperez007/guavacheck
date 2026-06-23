"use client";

import { useEffect, useState } from "react";

export default function AustinSidebar() {
  const [ws, setWs] = useState<WebSocket | null>(null);
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState<any[]>([]);

  useEffect(() => {
    const socket = new WebSocket("ws://127.0.0.1:8000/ws/austin");

    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setMessages((prev) => [...prev, data]);
    };

    setWs(socket);

    return () => socket.close();
  }, []);

  const sendMessage = () => {
    if (!ws || !input.trim()) return;

    ws.send(
      JSON.stringify({
        query: input,
        user_id: "test-user"
      })
    );

    setInput("");
  };

  return (
    <div style={{
      width: 400,
      height: "100vh",
      background: "#0a0a0a",
      color: "white",
      display: "flex",
      flexDirection: "column"
    }}>
      
      <div style={{ flex: 1, overflowY: "auto", padding: 10 }}>
        {messages.map((m, i) => (
          <pre key={i} style={{ fontSize: 12 }}>
            {JSON.stringify(m, null, 2)}
          </pre>
        ))}
      </div>

      <div style={{ padding: 10, display: "flex", gap: 5 }}>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask Austin..."
          style={{ flex: 1 }}
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}









