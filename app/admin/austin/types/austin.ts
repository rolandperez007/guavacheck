export interface AustinMessage {
  id: string;
  role: "user" | "assistant" | "system";
  content: string;
  timestamp: string;
}

export interface AustinRequest {
  message: string;
}

export interface AustinResponse {
  success: boolean;
  response: string;
  thinking?: string[];
  execution_time?: number;
}

export interface AustinHealth {
  status: string;
  version: string;
}
