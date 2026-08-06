import { useState } from "react";

export function useAustin() {
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);

  const runAustin = async (input: string) => {
    setLoading(true);
    setError(null);

    try {
      const res = await fetch("/api/austin/execute", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ input }),
      });

      const json = await res.json();

      if (!json.success) {
        throw new Error(json.error);
      }

      setData(json.result);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return {
    runAustin,
    loading,
    data,
    error,
  };
}
