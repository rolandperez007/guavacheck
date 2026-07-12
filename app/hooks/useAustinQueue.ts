"use client";

import { useEffect, useState } from "react";
import { QueueSummary } from "../admin/austin/types";

export function useAustinQueue() {
  const [queue, setQueue] = useState<QueueSummary | null>(null);
  const [loading, setLoading] = useState(true);

  async function load() {
    try {
      const response = await fetch("http://127.0.0.1:8000/austin/queue");
      const data = await response.json();

      setQueue(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    load();
  }, []);

  return {
    queue,
    loading,
    refresh: load,
  };
}