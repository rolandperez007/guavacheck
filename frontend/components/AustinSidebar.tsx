"use client";
import { useEffect, useState } from "react";

export default function AustinSidebar() {
  const [ws, setWs] = useState<WebSocket | null>(null);
  const [messages, setMessages] = useState<any[]>([]);
  const [input, setInput] = useState("");

  useEffect(() => {
    const socket = new WebSocket("ws://127.0.0.1:8000/ws/austin");

    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setMessages((prev) => [...prev, data]);
    };

    setWs(socket);
  }, []);

  const sendQuery = () => {
    if (!ws) return;

    ws.send(
      JSON.stringify({
        query: input,
        user_id: "test-user",
      })
    );

    setInput("");
  };

  return (
    <div style={{ width: 400, height: "100vh", background: "#000", color: "#fff" }}>
      <div style={{ height: "90%", overflow: "auto" }}>
        {messages.map((m, i) => (
          <pre key={i}>{JSON.stringify(m, null, 2)}</pre>
        ))}
      </div>

      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Ask Austin..."
      />
      <button onClick={sendQuery}>Send</button>
    </div>
  );
}


