# Interfaces and Concurrency

Sources: [`decisions.md#interfaces`](https://github.com/google/styleguide/blob/gh-pages/go/decisions.md#interfaces), [`best-practices.md#interfaces`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#interfaces), and [`best-practices.md#global-state`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#global-state).

## GO-API-001: Put interfaces near consumers

Define a small interface where it is consumed when the consumer needs substitution or isolation. A named interface is justified when existing logic must work with multiple implementations, a consumer needs only a narrow portion of a large API, or a real package dependency must be decoupled. Do not create one because a type is called a service or repository, to predict future implementations, or only to expose a test back door.

Keep the interface unexported when only one package consumes it. A producer should own and export an interface when the interface itself is the shared protocol or product, when many consumers require one canonical contract, or when generated schema defines the boundary. Before using an interface to break an import cycle, recheck the package split.

## GO-API-002: Keep interfaces minimal

Expose the smallest behavior set that supports the caller. Split an interface when unrelated responsibilities or independent lifetimes make implementations difficult to reason about.

Document an interface's contract, edge cases, ownership, and expected errors. Do not add an interface, mock, or exported test double solely to make a concrete implementation easy to fake; use the real implementation and public API when that gives a more faithful test.

## GO-API-003: Use canonical interface and method names

Name a one-method interface after its behavior, commonly with an `-er` form such as `Reader`, `Writer`, or `Formatter`. Use established method names and signatures such as `Read`, `Write`, `Close`, `Flush`, and `String` only for their conventional meanings; do not add an `I` prefix or invent a near-synonym for a standard contract.

## GO-API-004: Accept narrow interfaces and return concrete types by default

Accept the smallest interface the implementation actually uses, allowing callers to supply their own concrete types without adapter layers. Return a concrete type when callers may reasonably need its full behavior or when one implementation is the honest abstraction.

Return an interface only when the interface is the caller-visible contract: the implementation varies at runtime, exposing extra methods would bypass an invariant, or a package boundary cannot otherwise remain acyclic. Do not return an interface merely to hide a concrete type or reserve hypothetical flexibility.

## GO-STATE-001: Pass stateful dependencies explicitly

Libraries that maintain configuration, registrations, clients, clocks, or other observable state should expose instance values and accept them through constructors, parameters, methods, or struct fields. Explicit instances permit multiple independent configurations, hermetic tests, predictable initialization, and caller-owned concurrency. Avoid package-level setters, registries, replaceable clients, and lazy singletons whose behavior changes for every importer.

Package state is acceptable when it is logically constant or observably stateless, process-local, and not something callers need to replace. If convenience requires a default instance, also expose isolated instances, make package functions thin proxies, keep library dependencies on the explicit API, document lifecycle and concurrency, and provide a supported way to restore a known default for tests.

## GO-CONC-001: Make goroutine lifetimes explicit

For every goroutine, identify who starts it, what stops it, how errors are surfaced, and what synchronization proves completion. Prefer structured ownership with `context`, channels, `sync.WaitGroup`, or an existing project-approved coordination primitive.

## GO-CONC-002: Avoid goroutine leaks

Ensure blocked sends, receives, timers, and network operations can exit when the caller cancels. Do not start background work that outlives its owner without a documented lifecycle and shutdown path.

## GO-CONC-003: Use channels for communication, mutexes for state

Choose the simplest synchronization primitive that matches the problem. Use a mutex to protect shared state and a channel to coordinate ownership or transfer values; do not use either as decoration.

## GO-CONC-004: Make zero values useful where practical

Design types so their zero value is safe and meaningful when doing so does not obscure required invariants. Document constructors when initialization is mandatory.

## GO-CONC-005: Avoid accidental shared mutable state

Keep mutable state close to its owner. Treat package globals, shared maps, and reused buffers as concurrency boundaries that require explicit synchronization and tests.

## GO-CONC-006: Close channels only as part of an owned protocol

The sender that owns a channel's lifecycle should close it when closure communicates completion. Receivers should generally not close channels, and code must ensure no sender can race with closure or send after close.
