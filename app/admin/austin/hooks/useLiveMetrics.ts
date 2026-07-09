"use client";

import { useEffect, useState } from "react";
import type { LiveMetric } from "../types/metrics";
import { getLiveMetrics } from "../services/metrics.service";


export function useLiveMetrics(interval = 5000) {

  const [metrics, setMetrics] =
    useState<LiveMetric | null>(null);

  const [loading, setLoading] =
    useState(true);


  async function refreshMetrics() {

    setLoading(true);

    const response =
      await getLiveMetrics();


    if (response.success) {
      setMetrics(response.data);
    }


    setLoading(false);
  }


  useEffect(() => {

    refreshMetrics();


    const timer =
      setInterval(
        refreshMetrics,
        interval
      );


    return () =>
      clearInterval(timer);


  }, [interval]);


  return {
    metrics,
    loading,
    refreshMetrics,
  };
}