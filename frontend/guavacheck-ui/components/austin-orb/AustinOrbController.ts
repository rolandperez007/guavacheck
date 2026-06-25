Set-Content components\austin-orb\AustinOrbController.ts @"
import { AustinState } from './AustinOrbStates';

export class AustinOrbController {
  private state: AustinState = 'idle';

  getState() {
    return this.state;
  }

  setState(newState: AustinState) {
    this.state = newState;
  }

  onUserSpeak() {
    this.state = 'listening';
  }

  onThinking() {
    this.state = 'thinking';
  }

  onProcessing() {
    this.state = 'processing';
  }

  onError() {
    this.state = 'error';
  }

  reset() {
    this.state = 'idle';
  }
}
"@