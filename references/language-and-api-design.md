# Language and API Design

Sources: [`decisions.md#language`](https://github.com/google/styleguide/blob/gh-pages/go/decisions.md#language), [`decisions.md#named-result-parameters`](https://github.com/google/styleguide/blob/gh-pages/go/decisions.md#named-result-parameters), [`best-practices.md#function-argument-lists`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#function-argument-lists), [`best-practices.md#variable-declarations`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#variable-declarations), and [`best-practices.md#string-concatenation`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#string-concatenation).

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

Keep function signatures small, typed, and easy to read at common call sites. Prefer ordinary parameters while their roles remain distinct; split a function into use-case-specific operations when one signature is serving unrelated modes. Never place `context.Context` inside an options type: pass it first.

Use an options struct when many callers set several related values, field names prevent same-type or boolean mistakes, options are shared across calls, or per-field documentation matters. Use functional options only when most callers accept defaults, many options are sparse, option construction needs arguments or validation, and the added functions and closure machinery earn their cost. Functional options should accept explicit boolean or enum values when callers may choose dynamically and should normally apply in order with the last non-cumulative value winning. Do not use either pattern to disguise a simple call.

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

## GO-LANG-011: Name results only when the signature gains meaning

Name result parameters when equal-typed results need disambiguation, a caller must act on one result such as a cancel function, or a deferred closure must update the result. Prefer unnamed results when the function name and types already explain them. Do not name results merely to avoid a local declaration or enable a naked return; use naked returns only in short functions where the returned values remain obvious.

## GO-LANG-012: Choose declarations to reveal initialization intent

Use `:=` for a new non-zero local value, `var` when the zero value is intentionally ready for later use, and a composite literal when initial members are known. Initialize maps before writing. Add slice or map capacity only when the final or typical size is known or measurement justifies it; speculative preallocation can waste memory and is not a readability requirement. Specify channel direction in parameters and results when the API only sends or receives so the type exposes ownership and the compiler rejects accidental misuse.

## GO-LANG-013: Match string construction to the operation

Use `+` for a small fixed concatenation, `fmt.Sprintf` when format verbs make interpolation clearer, and `strings.Builder` when constructing a string incrementally in a loop or across many writes. Adjacent constant expressions are combined at compile time, so keep long constant text readable without introducing runtime machinery. Do not choose a builder for a single expression or split a literal solely to satisfy a line width preference.
