export class WorldClock {

  private start = Date.now();

  getTime() {

    return Date.now() - this.start;

  }

  getDayProgress() {

    return ((this.getTime() / 1000) % 300) / 300;

  }

}

export const worldClock = new WorldClock();