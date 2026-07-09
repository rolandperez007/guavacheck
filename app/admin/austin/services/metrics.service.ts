import type {
  MetricsResponse
} from "../types/metrics";


const API_URL =
  process.env.NEXT_PUBLIC_AUSTIN_API_URL ||
  "http://127.0.0.1:8000";


export async function getLiveMetrics(): Promise<MetricsResponse> {

  try {

    const response = await fetch(
      `${API_URL}/metrics`,
      {
        method: "GET",
        cache: "no-store",
      }
    );


    if (!response.ok) {
      throw new Error(
        `Metrics request failed: ${response.status}`
      );
    }


    const data = await response.json();


    return {
      success: true,
      data,
    };


  } catch(error) {


    return {
      success: false,

      error:
        error instanceof Error
          ? error.message
          : "Unknown metrics error",

      data: {
        timestamp:
          new Date().toISOString(),

        cpu: 0,
        memory: 0,
        requests: 0,

        engines: [],

        queue: {
          pending: 0,
          processing: 0,
          completed: 0,
          failed: 0,
        },

        memoryStats: {
          total: 0,
          used: 0,
          free: 0,
        },
      },
    };
  }
}