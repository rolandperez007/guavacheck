"use client";

import { useState } from "react";

interface Props {
  onSend(message: string): void;
}

export default function AustinInput({ onSend }: Props) {
  const [message, setMessage] = useState("");

  function submit() {
    if (!message.trim()) return;

    onSend(message);

    setMessage("");
  }

  return (
    <div className="flex gap-3 border-t border-slate-800 p-4">
      <input
        className="flex-1 rounded-lg bg-[#101d2d] px-4 py-3 text-white outline-none"
        placeholder="Ask Austin anything..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") submit();
        }}
      />

      <button
        onClick={submit}
        className="rounded-lg bg-emerald-600 px-6 py-3 font-semibold hover:bg-emerald-500"
      >
        Send
      </button>
    </div>
  );
}
