/** @type {import('next').NextConfig} */
module.exports = {
  reactStrictMode: true,
  poweredByHeader: false,
  trailingSlash: false,

  pageExtensions: ["ts", "tsx", "js", "jsx"],

  webpack: (config) => {
    config.watchOptions = {
      ignored: ["**/mobile-app-disabled/**"],
    };
    return config;
  },
};
