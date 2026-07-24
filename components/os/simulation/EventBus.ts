export type SimulationEvent = {
  id: string;
  type: string;
  timestamp: number;
  payload?: unknown;
};

type Listener = (event: SimulationEvent) => void;

class EventBus {

  private listeners = new Map<string, Listener[]>();

  emit(event: SimulationEvent) {

    const list = this.listeners.get(event.type);

    if (!list) return;

    list.forEach(listener => listener(event));

  }

  subscribe(type: string, listener: Listener) {

    const list = this.listeners.get(type) ?? [];

    list.push(listener);

    this.listeners.set(type, list);

    return () => {

      const updated = (this.listeners.get(type) ?? []).filter(l => l !== listener);

      this.listeners.set(type, updated);

    };

  }

}

export const eventBus = new EventBus();