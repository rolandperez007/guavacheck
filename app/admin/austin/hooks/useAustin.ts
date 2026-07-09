"use client";

import { useState } from "react";
import AustinService from "../services/austin.service";
import { AustinMessage } from "../types/austin";

export default function useAustin() {

  const [messages, setMessages] =
    useState<AustinMessage[]>([]);

  const [loading, setLoading] =
    useState(false);

  async function send(message: string) {

    const userMessage: AustinMessage = {

      id: crypto.randomUUID(),

      role: "user",

      content: message,

      timestamp: new Date().toISOString(),

    };

    setMessages((previous) => [
      ...previous,
      userMessage,
    ]);

    setLoading(true);

    try {

      const result =
        await AustinService.send({
          message,
        });

      const assistantMessage: AustinMessage = {

        id: crypto.randomUUID(),

        role: "assistant",

        content:
          result.response ??
          "Austin completed successfully.",

        timestamp:
          new Date().toISOString(),

      };

      setMessages((previous) => [
        ...previous,
        assistantMessage,
      ]);

    } catch (error) {

      setMessages((previous) => [

        ...previous,

        {

          id: crypto.randomUUID(),

          role: "system",

          content:
            "Unable to contact Austin backend.",

          timestamp:
            new Date().toISOString(),

        },

      ]);

      console.error(error);

    } finally {

      setLoading(false);

    }

  }

  return {

    loading,

    messages,

    send,

  };

}