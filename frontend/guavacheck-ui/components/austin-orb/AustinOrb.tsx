Set-Content components\austin-orb\AustinOrb.tsx @"
import React from 'react';
import './orb.css';

export type AustinState =
  | 'idle'
  | 'thinking'
  | 'listening'
  | 'processing'
  | 'error';

interface Props {
  state: AustinState;
}

export default function AustinOrb({ state }: Props) {
  return (
    <div className={`austin-orb ${state}`}>
      <div className="core" />
      <div className="ring" />
    </div>
  );
}
"@