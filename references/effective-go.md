# Effective Go Core Language Idioms

Source: [Effective Go](https://go.dev/doc/effective_go), the Go project's core language and idiom guide.

Effective Go was written for an early Go release and is not actively updated. Use this reference for language mechanics and established idioms, but prefer the current Go specification, standard-library documentation, current Google Go Style Guide guidance, and repository-local rules when they differ. This reference does not define modern guidance for generics, modules, or newer APIs.

## GO-EFFECTIVE-001: Keep short declarations and scope obvious

Use `:=` when it makes local initialization clear. Remember that a short declaration may redeclare variables only when those variables were declared earlier in the same block and at least one non-blank variable is new; avoid shadowing that hides an outer value or changes which error a later branch observes.

## GO-EFFECTIVE-002: Use idiomatic control structures

Write conditions without redundant parentheses, use `for` for all loop forms, and use `switch` to make mutually exclusive cases explicit. Use a type switch or type assertion only when the dynamic type is part of the contract, and handle the failed assertion case deliberately.

## GO-EFFECTIVE-003: Keep multiple returns and named results readable

Use multiple return values to keep success data and errors explicit. Use named result parameters when they document the result or make a short deferred operation clearer; avoid them when they hide the returned value or make control flow harder to follow.

## GO-EFFECTIVE-004: Defer cleanup at the ownership boundary

After successfully acquiring a resource, defer its cleanup close to the acquisition when the surrounding function owns the resource. Do not use `defer` in an unbounded loop when it would retain resources until the outer function returns, and handle a meaningful cleanup error according to the operation's error policy.

## GO-EFFECTIVE-005: Choose allocation forms by the value needed

Use `new(T)` when a pointer to a zero value is what the API needs. Use `make` to initialize slices, maps, and channels, which are returned as their value types. Prefer a composite literal or a named constructor when it makes required fields and invariants clearer.

## GO-EFFECTIVE-006: Treat slices as descriptors with shared storage

Remember that a slice contains a pointer, length, and capacity and may share an array with other slices. `append` may allocate a new backing array, so always use its returned slice. Make ownership and aliasing clear when a function retains or mutates a slice.

## GO-EFFECTIVE-007: Initialize maps before writing and check optional entries

Reads from a nil map are safe, but writes require an initialized map. Use a map literal or `make` before writes, and use the comma-ok form when a missing key is distinct from a stored zero value. Do not depend on map iteration order.

## GO-EFFECTIVE-008: Keep zero values and initialization predictable

Prefer useful zero values when practical. Keep required initialization in an explicit constructor or setup path, and use `init` only for small, deterministic package initialization whose ordering and side effects are easy to reason about.

## GO-EFFECTIVE-009: Keep receiver and copying choices consistent

Use pointer receivers for mutation, identity, large state, or types that must not be copied. Use value receivers for small immutable values. Keep the choice consistent across a type and never copy a value containing synchronization state after first use.

## GO-EFFECTIVE-010: Use interfaces through implicit satisfaction

A concrete type satisfies an interface by implementing its methods; no declaration is required. Keep interfaces small and consumer-oriented. Use comma-ok assertions when a value may not implement an optional interface, and do not recover a concrete type when the interface contract is sufficient.

## GO-EFFECTIVE-011: Treat embedding as composition and API surface

Embedding promotes methods and, for structs, fields; it is composition rather than inheritance. Embed only when the promoted behavior belongs in the containing type's API, and use a named field when explicit ownership or a narrower surface is clearer.

## GO-EFFECTIVE-012: Make channel ownership and goroutine lifetimes explicit

Use goroutines for concurrent work with a clear owner and completion path. Use channels to communicate values or transfer ownership, use directional channel types to document roles, and close a channel only by the side that owns sending when closure is part of the protocol.

## GO-EFFECTIVE-013: Keep the blank identifier intentional

Use `_` only when discarding a value is intentional, such as an unneeded range value, a deliberately side-effect-only import, or a compile-time interface check. Never use it to hide an error or an otherwise required result; document side-effect imports and keep them rare.

## GO-EFFECTIVE-014: Return errors for ordinary failures

Use error values for expected failures and add context at the boundary that owns the operation. Reserve `panic` for unrecoverable programmer invariants. Recover only at a deliberate package or process boundary that can restore a useful error or response; do not use `recover` as routine control flow.

## GO-EFFECTIVE-015: Make formatting and string behavior conventional

Let `gofmt` control source layout. Implement `String() string` only when a type has a stable, useful display form, and keep formatting methods free of surprising side effects or error-dependent behavior.
