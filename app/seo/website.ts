export const website = {
  "@context": "https://schema.org",

  "@type": "WebSite",

  name: "guavacheck",

  url: "https://www.guavacheck.com",

  description: "Global AI Property Intelligence Platform",

  inLanguage: ["en", "fr", "es", "de", "pt", "ar", "zh"],

  potentialAction: {
    "@type": "SearchAction",

    target: "https://www.guavacheck.com/search?q={search_term_string}",

    "query-input": "required name=search_term_string",
  },
};
