Set-Content state\austinState.ts @"
export const AustinStateMachine = {
  idle: 'idle',
  thinking: 'thinking',
  listening: 'listening',
  processing: 'processing',
  error: 'error',
} as const;

export type AustinState =
  typeof AustinStateMachine[keyof typeof AustinStateMachine];
"@