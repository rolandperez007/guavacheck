const BASE_URL = "https://www.guavacheck.com";

export function canonical(path = ""): string {
  if (!path || path === "/") {
    return BASE_URL;
  }

  return `${BASE_URL}${path}`;
}
