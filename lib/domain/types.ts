export interface DomainMessage {
  type: string;

  payload: any;

  timestamp: number;
}

export interface DomainModule {
  initialize(): void;

  destroy(): void;

  handle(message: DomainMessage): void;
}
