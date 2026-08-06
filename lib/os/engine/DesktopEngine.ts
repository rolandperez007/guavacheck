export interface DesktopApplication {
  id: string;

  title: string;

  icon: string;

  component: string;

  width: number;

  height: number;

  x: number;

  y: number;

  minimized: boolean;

  maximized: boolean;

  focused: boolean;
}

class DesktopEngine {
  private apps: DesktopApplication[] = [];

  register(app: DesktopApplication) {
    this.apps.push(app);
  }

  getApplications() {
    return this.apps;
  }
}

export const desktopEngine = new DesktopEngine();
