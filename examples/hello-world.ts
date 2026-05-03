/**
 * Minimal TypeScript HelloWorld smoke test for ScoutFlow.
 *
 * Run with a TS runtime such as `tsx` or compile with `tsc` first.
 */
export function helloWorld(name: string = 'ScoutFlow'): string {
  return `Hello, ${name}!`;
}

const message = helloWorld();
console.log(message);
