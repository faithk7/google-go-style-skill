# Language and API Design

Sources: [`decisions.md`](https://github.com/google/styleguide/blob/gh-pages/go/decisions.md#language) and [`best-practices.md`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#function-argument-lists).

## GO-LANG-001: Prefer direct control flow

Use ordinary `if`, `for`, and `switch` forms when they make the state transition clear. Avoid clever expressions, unnecessary named results, and dense one-liners that make debugging or review harder.

## GO-LANG-002: Preserve nil semantics deliberately

Choose nil versus empty slices, maps, pointers, and interfaces based on the API contract. Document meaningful distinctions and test both states when callers can observe them.

For local empty slices, prefer the nil zero value unless an API or serialization contract requires a non-nil empty slice; `len`, `cap`, ranging, and `append` work normally on nil slices.

## GO-LANG-003: Do not panic for ordinary failures

Return errors for input, I/O, network, configuration, and dependency failures. Reserve panics for unrecoverable programmer invariants or narrowly scoped initialization checks, and prefer an explicit `Must` function only when its contract is clear.

`MustX` helpers are appropriate for startup or package initialization (and tightly scoped test setup), not for user input or recoverable operational failures.

## GO-LANG-004: Pass values and pointers intentionally

Pass small immutable values by value. Use pointers when mutation, identity, large state, or nil semantics matter. Keep receiver type choices consistent across a type and avoid copying synchronization objects, pointer-receiver values, or external types whose internal buffers may alias.

## GO-LANG-005: Design arguments for clarity

Keep function signatures small and typed. Use an options structure when configuration is genuinely extensible or has several independent fields; do not use variadic options to hide a simple call.

## GO-LANG-006: Use generics only for real type relationships

Use generics when one algorithm or data structure must preserve a meaningful relationship across types. Prefer concrete code when generic constraints would make the API or error messages harder to understand.

Document exported generic APIs and avoid using generics to create a DSL, assertion framework, or error-handling layer. Where a unifying interface already expresses the contract, do not add type parameters merely to avoid an interface.

## GO-LANG-007: Prefer synchronous APIs by default

A function should normally finish its work and return its result before returning. Keep goroutines and channel coordination inside the call so callers can test and reason about completion; make asynchronous behavior, ownership, cancellation, and callbacks explicit when it is required.

## GO-LANG-008: Use type aliases only for compatibility

Use `type New Old` to define a distinct type and `type New = Old` only to refer to an existing type. Type aliases are uncommon and primarily support package or source migrations; do not use one where a new type or no declaration is clearer.

## GO-LANG-009: Prefer `any` in new code where an empty interface is intended

For Go versions that support it, use `any` instead of `interface{}` when the value intentionally accepts any type. Do not introduce it when the repository targets an older Go version or when a more precise type, interface, or type parameter expresses the contract.

## GO-LANG-010: Do not add redundant `switch` breaks

Go `switch` cases stop automatically. Omit unlabeled `break` statements at the end of cases; use `fallthrough` only when the cross-case behavior is deliberate, and use a labeled break when leaving an enclosing loop.
