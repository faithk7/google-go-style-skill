# Effective Go Core Language Idioms

Source: [Effective Go](https://go.dev/doc/effective_go), the Go project's core language and idiom guide.

Effective Go was written for an early Go release and is not actively updated. Use this reference for language mechanics and established idioms, but prefer the current Go specification, standard-library documentation, current Google Go Style Guide guidance, and repository-local rules when they differ. This reference does not define modern guidance for generics, modules, or newer APIs.

This is a crosswalk, not a replacement for the source document. Rules describing compiler or runtime behavior are semantic requirements. Rules describing names, allocation style, initialization, concurrency structure, or examples are `Should` guidance unless the current Google baseline or a repository rule makes the decision explicit.

## Coverage map

| Effective Go section | Local guidance |
| --- | --- |
| Introduction; Examples | `GO-PRINCIPLE-*`; `GO-DOC-003` |
| Formatting; Commentary | `GO-FMT-*`; `GO-COMMENT-*` |
| Names; Package names; Getters; Interface names; MixedCaps | `GO-NAME-*`; `GO-API-003` |
| Semicolons; Control structures; If; Redeclaration and reassignment; For; Switch; Type switch | `GO-EFFECTIVE-001`; `GO-EFFECTIVE-002`; `GO-EFFECTIVE-016` |
| Functions; Multiple return values; Named result parameters; Defer | `GO-EFFECTIVE-003`; `GO-EFFECTIVE-004`; `GO-ERR-*` |
| Data; Allocation with `new`; Constructors and composite literals; Allocation with `make` | `GO-EFFECTIVE-005`; `GO-EFFECTIVE-016`; `GO-PRINCIPLE-006` |
| Arrays; Slices; Two-dimensional slices; Maps; Append | `GO-EFFECTIVE-006`; `GO-EFFECTIVE-007`; `GO-EFFECTIVE-017` |
| Printing | `GO-EFFECTIVE-015`; `GO-FMT-006` |
| Initialization; Constants; Variables; The `init` function | `GO-EFFECTIVE-008`; `GO-NAME-005`; `GO-NAME-009` |
| Methods; Pointers vs. Values | `GO-EFFECTIVE-009`; `GO-LANG-004` |
| Interfaces and other types; Conversions; Interface conversions and type assertions; Generality; Interfaces and methods | `GO-EFFECTIVE-010`; `GO-EFFECTIVE-018`; `GO-API-*`; `GO-LANG-006`; `GO-LANG-009` |
| The blank identifier; The blank identifier in multiple assignment; Unused imports and variables; Import for side effect; Interface checks | `GO-EFFECTIVE-013`; `GO-FMT-002`; `GO-TEST-*` |
| Embedding | `GO-EFFECTIVE-011` |
| Concurrency; Share by communicating; Goroutines; Channels; Channels of channels; Parallelization; A leaky buffer | `GO-EFFECTIVE-012`; `GO-EFFECTIVE-019`; `GO-CONC-*` |
| Errors; Panic; Recover | `GO-EFFECTIVE-014`; `GO-ERR-*`; `GO-LANG-003` |
| A web server | `GO-CTX-*`; `GO-CONC-*`; `GO-ERR-*`; `GO-LIB-*` |

## Conflict guide

| Topic | Resolution |
| --- | --- |
| Language or runtime behavior | Use the current Go specification and standard-library documentation. Treat Effective Go examples as illustrations of the core model, not as a versioned specification. |
| Generics, modules, `any`, and newer APIs | Use the current Google rules and the repository's supported Go version. Effective Go does not define guidance for these features. |
| Nil versus empty slices | Preserve the caller-visible API or serialization contract. Prefer the nil zero value locally only when callers cannot observe a required distinction. |
| `new`, `make`, and empty composite literals | Follow their actual type and initialization semantics. Where forms are equivalent, this is a local-consistency choice rather than a review defect. |
| Package initialization and `init` | Prefer explicit construction and startup wiring. Use `init` only for small deterministic registration or initialization that cannot be expressed more clearly at an owned boundary. |
| Error origin and wrapping | Preserve stable public formats when compatibility requires them; otherwise prefer `%w`, `errors.Is`/`errors.As`, and structured context over parseable strings or redundant prefixes. |
| `panic` and `recover` | Return errors for ordinary failures. Permit tightly coupled internal panic/recover only when it is converted at the package boundary and cannot suppress an unknown or corrupted state. |
| Concurrency examples | Preserve the communication model, but add current ownership, cancellation, completion, and leak-prevention requirements. Prefer a synchronous API when callers can add concurrency themselves. |
| Historical library or server examples | Use current packages, security practices, contexts, and APIs. Do not copy obsolete endpoints, architecture, or error-handling patterns merely because they appear in the tutorial. |

## GO-EFFECTIVE-001: Keep short declarations and scope obvious

Use `:=` when it makes local initialization clear. Remember that a short declaration may redeclare variables only when those variables were declared earlier in the same block and at least one non-blank variable is new; avoid shadowing that hides an outer value or changes which error a later branch observes.

## GO-EFFECTIVE-002: Use idiomatic control structures

Write conditions without redundant parentheses, use `for` for all loop forms, and use `switch` to make mutually exclusive cases explicit. Use `select` to coordinate channel operations. Use a type switch or type assertion only when the dynamic type is part of the contract, and handle the failed assertion case deliberately.

## GO-EFFECTIVE-003: Keep multiple returns and named results readable

Use multiple return values to keep success data and errors explicit. Use named result parameters when they document the result or make a short deferred operation clearer; avoid them when they hide the returned value or make control flow harder to follow.

## GO-EFFECTIVE-004: Defer cleanup at the ownership boundary

After successfully acquiring a resource, defer its cleanup close to the acquisition when the surrounding function owns the resource. Do not use `defer` in an unbounded loop when it would retain resources until the outer function returns, and handle a meaningful cleanup error according to the operation's error policy.

## GO-EFFECTIVE-005: Choose allocation forms by the value needed

Use `new(T)` when a pointer to a zero value is what the API needs. Use `make` to initialize slices, maps, and channels, which are returned as their value types. Prefer a composite literal or a named constructor when it makes required fields and invariants clearer.

Do not infer a universal preference between equivalent zero-value declarations, empty composite literals, and `new` or `make`; choose the clearest locally consistent form unless the resulting type or initialization behavior differs.

## GO-EFFECTIVE-006: Treat slices as descriptors with shared storage

Remember that a slice contains a pointer, length, and capacity and may share an array with other slices. `append` may allocate a new backing array, so always use its returned slice. Make ownership and aliasing clear when a function retains or mutates a slice.

Prefer slices for variable-length sequences and use arrays when fixed size, value-copy semantics, or an explicitly shaped data layout is part of the contract. A two-dimensional slice is a slice of independently sized slices unless the implementation deliberately shares one backing allocation.

## GO-EFFECTIVE-007: Initialize maps before writing and check optional entries

Reads from a nil map are safe, but writes require an initialized map. Use a map literal or `make` before writes, and use the comma-ok form when a missing key is distinct from a stored zero value. Do not depend on map iteration order.

## GO-EFFECTIVE-008: Keep zero values and initialization predictable

Prefer useful zero values when practical. Keep required initialization in an explicit constructor or setup path, and use `init` only for small, deterministic package initialization whose ordering and side effects are easy to reason about.

## GO-EFFECTIVE-009: Keep receiver and copying choices consistent

Use pointer receivers for mutation, identity, large state, or types that must not be copied. Use value receivers for small immutable values. Keep the choice consistent across a type and never copy a value containing synchronization state after first use.

## GO-EFFECTIVE-010: Use interfaces through implicit satisfaction

A concrete type satisfies an interface by implementing its methods; no declaration is required. Keep interfaces small and consumer-oriented. Use comma-ok assertions when a value may not implement an optional interface, and do not recover a concrete type when the interface contract is sufficient. Use canonical method names and signatures such as `Read`, `Write`, `Close`, and `String` when the behavior is the same.

## GO-EFFECTIVE-011: Treat embedding as composition and API surface

Embedding promotes methods and, for structs, fields; it is composition rather than inheritance. Embed only when the promoted behavior belongs in the containing type's API, and use a named field when explicit ownership or a narrower surface is clearer.

## GO-EFFECTIVE-012: Make channel ownership and goroutine lifetimes explicit

Use goroutines for concurrent work with a clear owner and completion path. Use channels to communicate values or transfer ownership, use directional channel types to document roles, and close a channel only by the side that owns sending when closure is part of the protocol.

## GO-EFFECTIVE-013: Keep the blank identifier intentional

Use `_` only when discarding a value is intentional, such as an unneeded range value, a deliberately side-effect-only import, or a compile-time interface check. Never use it to hide an error or an otherwise required result; document side-effect imports and keep them rare.

## GO-EFFECTIVE-014: Return errors for ordinary failures

Use error values for expected failures and add context at the boundary that owns the operation. Reserve `panic` for unrecoverable programmer invariants. Recover only at a deliberate package boundary that can restore a useful error or response, and never allow an internal panic to escape as an undocumented API behavior. Do not use `recover` as routine control flow or as a general crash-suppression mechanism.

## GO-EFFECTIVE-015: Make formatting and string behavior conventional

Let `gofmt` control source layout. Implement `String() string` only when a type has a stable, useful display form, and keep formatting methods free of surprising side effects or error-dependent behavior.

## GO-EFFECTIVE-016: Keep semicolon insertion and braces idiomatic

Do not write statement-separating semicolons except where the grammar requires them, such as `for` clauses or multiple statements on one line. Keep the opening brace on the same line as `if`, `for`, `switch`, `select`, and function declarations; let `gofmt` preserve the standard layout.

## GO-EFFECTIVE-017: Make initialization and backing storage explicit

Design useful zero values when practical, but use constructors when invariants require setup. For slices and maps, make capacity, aliasing, and ownership explicit when they affect behavior. Do not use `init` to hide ordinary dependency setup or ordering-sensitive side effects.

## GO-EFFECTIVE-018: Use conversions and method sets deliberately

A conversion changes the value's type and may change representation or semantics; an assertion tests an interface's dynamic value and may fail. Choose pointer or value receivers based on the method sets an API must satisfy, and use explicit compile-time interface checks only when they document an important contract.

## GO-EFFECTIVE-019: Use channels to coordinate bounded work

Use unbuffered channels when communication should also synchronize completion, buffered channels when a bounded queue or semaphore is the contract, and `select` for cancellation, timeouts, or non-blocking alternatives. Keep channel-valued requests and buffer-reuse schemes under explicit ownership and cleanup rules; do not use them to obscure a simpler synchronous function.
