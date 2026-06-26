import { useEffect, useState } from 'react';
import { AustinState } from '../components/austin-orb/AustinOrbStates';

export default function useAustinDemo() {
  const [state, setState] = useState<AustinState>('idle');

  useEffect(() => {
    const sequence = async () => {
      while (true) {
        setState('listening');
        await wait(2000);

        setState('thinking');
        await wait(2500);

        setState('processing');
        await wait(3000);

        setState('idle');
        await wait(2000);
      }
    };

    sequence();
  }, []);

  return { state };
}

const wait = (ms: number) => new Promise(res => setTimeout(res, ms));
