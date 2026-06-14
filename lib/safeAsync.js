export function safeAsync(fn) {
  return async (...args) => {
    try {
      return await fn(...args);
    } catch (error) {
      console.error(error);
      return null;
    }
  };
}
