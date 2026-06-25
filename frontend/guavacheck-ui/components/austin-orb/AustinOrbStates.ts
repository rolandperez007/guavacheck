Set-Content components\austin-orb\AustinOrbStates.ts @"
export type AustinState =
  | 'idle'
  | 'thinking'
  | 'listening'
  | 'processing'
  | 'error';

export const AustinStateMeta = {
  idle: 'calm',
  thinking: 'slow pulse',
  listening: 'rhythmic pulse',
  processing: 'energy flow',
  error: 'flicker',
};
"@