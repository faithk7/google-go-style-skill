# Language and API Design

Sources: [`decisions.md`](https://github.com/google/styleguide/blob/gh-pages/go/decisions.md#language) and [`best-practices.md`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#function-argument-lists).

## GO-LANG-001: Prefer direct control flow

Use ordinary `if`, `for`, and `switch` forms when they make the state transition clear. Avoid clever expressions, unnecessary named results, and dense one-liners that make debugging or review harder.

## GO-LANG-002: Preserve nil semantics deliberately

Choose nil versus empty slices, maps, pointers, and interfaces based on the API contract. Document meaningful distinctions and test both states when callers can observe them.

## GO-LANG-003: Do not panic for ordinary failures

Return errors for input, I/O, network, configuration, and dependency failures. Reserve panics for unrecoverable programmer invariants or narrowly scoped initialization checks, and prefer an explicit `Must` function only when its contract is clear.

## GO-LANG-004: Pass values and pointers intentionally

Pass small immutable values by value. Use pointers when mutation, identity, large state, or nil semantics matter. Keep receiver type choices consistent across a type and avoid accidental copies of synchronization primitives.

## GO-LANG-005: Design arguments for clarity

Keep function signatures small and typed. Use an options structure when configuration is genuinely extensible or has several independent fields; do not use variadic options to hide a simple call.

## GO-LANG-006: Use generics only for real type relationships

Use generics when one algorithm or data structure must preserve a meaningful relationship across types. Prefer concrete code when generic constraints would make the API or error messages harder to understand.
