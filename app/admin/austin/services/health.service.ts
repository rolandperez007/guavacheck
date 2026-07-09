import type { HealthResponse } from "../types/health";

const API_URL =
  process.env.NEXT_PUBLIC_AUSTIN_API_URL ||
  "http://127.0.0.1:8000";


export async function getSystemHealth(): Promise<HealthResponse> {
  try {
    const response = await fetch(
      `${API_URL}/health`,
      {
        method: "GET",
        cache: "no-store",
      }
    );

    if (!response.ok) {
      throw new Error(
        `Health request failed: ${response.status}`
      );
    }

    const data = await response.json();

    return {
      success: true,
      data,
    };

  } catch (error) {

    return {
      success: false,
      error:
        error instanceof Error
          ? error.message
          : "Unknown health error",

      data: {
        overall: "offline",

        fastapi: {
          name: "FastAPI",
          status: "offline",
        },

        redis: {
          name: "Redis",
          status: "unknown",
        },

        postgres: {
          name: "PostgreSQL",
          status: "unknown",
        },

        websocket: {
          name: "WebSocket",
          status: "unknown",
        },
      },
    };
  }
}