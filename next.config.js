const path = require("path");

/** @type {import('next').NextConfig} */
module.exports = {
  reactStrictMode: true,
  poweredByHeader: false,
  trailingSlash: false,

  pageExtensions: ["ts", "tsx", "js", "jsx"],

  outputFileTracingRoot: path.join(__dirname),

  webpack: (config) => {
    config.watchOptions = {
      ignored: [
        "**/mobile-app-disabled/**",
      ],
    };

    return config;
  },
};

    
