# Interfaces and Concurrency

Sources: [`decisions.md`](https://github.com/google/styleguide/blob/gh-pages/go/decisions.md#interfaces) and [`best-practices.md`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#interfaces).

## GO-API-001: Put interfaces near consumers

Define a small interface where it is consumed when the consumer needs substitution or isolation. Do not create an interface for every concrete type or merely to predict future implementations. Return concrete types unless an interface is the actual contract callers need.

## GO-API-002: Keep interfaces minimal

Expose the smallest behavior set that supports the caller. Split an interface when unrelated responsibilities or independent lifetimes make implementations difficult to reason about.

Document an interface's contract, edge cases, ownership, and expected errors. Do not add an interface, mock, or exported test double solely to make a concrete implementation easy to fake; use the real implementation and public API when that gives a more faithful test.

## GO-API-003: Use canonical interface and method names

Name a one-method interface after its behavior, commonly with an `-er` form such as `Reader`, `Writer`, or `Formatter`. Use established method names and signatures such as `Read`, `Write`, `Close`, `Flush`, and `String` only for their conventional meanings; do not add an `I` prefix or invent a near-synonym for a standard contract.

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
