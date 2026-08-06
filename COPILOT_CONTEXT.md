## TypeScript Standards

The frontend uses:

- Next.js 15
- TypeScript 5
- ES Modules
- moduleResolution = bundler

Never generate:

- require(...)
- module.exports
- exports.*

Always use:

- import
- export
- export default

Prefer modern Node imports:

```ts
import fs from "node:fs";
import path from "node:path";
import { readFile } from "node:fs/promises";
```

Match the import style already used in the surrounding code.

Preserve strict typing and avoid `any` unless absolutely necessary.