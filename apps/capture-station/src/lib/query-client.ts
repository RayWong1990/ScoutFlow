type QueryLoader<T> = () => Promise<T>;

export type QueryClient = {
  get<T>(key: string, loader: QueryLoader<T>): Promise<T>;
  invalidate(key: string): void;
  clear(): void;
};

export function createQueryClient(): QueryClient {
  const cache = new Map<string, Promise<unknown>>();

  return {
    get<T>(key: string, loader: QueryLoader<T>) {
      const existing = cache.get(key) as Promise<T> | undefined;
      if (existing) {
        return existing;
      }

      const next = loader();
      cache.set(key, next);
      return next;
    },
    invalidate(key: string) {
      cache.delete(key);
    },
    clear() {
      cache.clear();
    }
  };
}
