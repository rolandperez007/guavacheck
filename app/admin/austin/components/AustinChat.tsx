"use client";

import { useState } from "react";
import AustinInput from "./AustinInput";

interface Message {

  role: "user" | "assistant";

  content: string;

}

export default function AustinChat() {

  const [messages, setMessages] = useState<Message[]>([
    {
      role: "assistant",
      content:
        "Good evening. I'm Austin. Engineering systems are online. How may I assist?"
    }
  ]);

  function send(message: string) {

    setMessages((prev) => [

      ...prev,

      {

        role: "user",

        content: message

      },

      {

        role: "assistant",

        content:
          "Backend connection coming next. For now I'm running in simulation mode."

      }

    ]);

  }

  return (

    <div className="flex h-full flex-col rounded-xl border border-slate-800 bg-[#0d1a28]">

      <div className="flex-1 overflow-y-auto p-5">

        {messages.map((msg, index) => (

          <div
            key={index}
            className={`mb-4 flex ${
              msg.role === "user"
                ? "justify-end"
                : "justify-start"
            }`}
          >

            <div
              className={`max-w-[75%] rounded-xl px-4 py-3 ${
                msg.role === "user"
                  ? "bg-emerald-600"
                  : "bg-[#16283b]"
              }`}
            >

              {msg.content}

            </div>

          </div>

        ))}

      </div>

      <AustinInput onSend={send} />

    </div>

  );

}