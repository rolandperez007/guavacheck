export const GA_MEASUREMENT_ID = "G-D1XB03RNNW";

declare global {
  interface Window {
    gtag: (...args: any[]) => void;
  }
}

export const pageView = (url: string) => {
  window.gtag?.("config", GA_MEASUREMENT_ID, {
    page_path: url,
  });
};

export const trackEvent = (
  action: string,
  params: Record<string, any> = {}
) => {
  window.gtag?.("event", action, params);
};