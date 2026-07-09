"use client";

import { useEffect, useState } from "react";
import type { SystemHealth } from "../types/health";
import { getSystemHealth } from "../services/health.service";


export function useSystemHealth(interval = 10000) {

  const [health, setHealth] = useState<SystemHealth | null>(null);
  const [loading, setLoading] = useState(true);


  async function refreshHealth() {

    setLoading(true);

    const response = await getSystemHealth();

    if (response.success) {
      setHealth(response.data);
    }

    setLoading(false);
  }


  useEffect(() => {

    refreshHealth();

    const timer = setInterval(
      refreshHealth,
      interval
    );

    return () => clearInterval(timer);

  }, [interval]);


  return {
    health,
    loading,
    refreshHealth,
  };
}