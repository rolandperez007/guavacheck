Set-Content hooks\useAustinState.ts @"
import { useState } from 'react';
import { AustinState } from '../components/austin-orb/AustinOrbStates';

export default function useAustinState() {
  const [state, setState] = useState<AustinState>('idle');

  return {
    state,
    setState,
    isIdle: state === 'idle',
    isThinking: state === 'thinking',
    isListening: state === 'listening',
    isProcessing: state === 'processing',
    isError: state === 'error',
  };
}
"@