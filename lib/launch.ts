/**
 * guavacheck Launch Configuration
 *
 * Controls public access while the platform is under active development.
 */

export const launchConfig = {
  /**
   * When TRUE:
   * - Homepage shows the Gateway.
   * - Unreleased routes redirect to Gateway.
   */
  launchMode: true,

  /**
   * Future feature flags.
   */
  features: {
    city: false,
    marketplace: false,
    community: false,
    builder: false,
    construction: false,
    verification: false,
    dashboard: false,
    developer: false,
    admin: false,
    enterprise: false,
    government: false,
    finance: false,
    propertyDNA: false,
    austinConsole: false,
  },
};

export default launchConfig;