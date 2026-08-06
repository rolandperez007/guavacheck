import { AustinHealth, AustinRequest, AustinResponse } from "../types/austin";

const BASE_URL = process.env.NEXT_PUBLIC_AUSTIN_API ?? "http://127.0.0.1:8000";

class AustinService {
  async send(request: AustinRequest): Promise<AustinResponse> {
    const response = await fetch(`${BASE_URL}/austin/execute`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(request),
    });

    if (!response.ok) {
      throw new Error("Austin backend unavailable");
    }

    return response.json();
  }

  async health(): Promise<AustinHealth> {
    const response = await fetch(`${BASE_URL}/`);

    return response.json();
  }
}

export default new AustinService();
