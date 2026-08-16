# Standard Library Composition

Sources: handwritten standard-library code sampled from pinned [`golang/go` commit `72aa6db7943024b48c4d41c1fbc32b57b9fa036e`](https://github.com/golang/go/tree/72aa6db7943024b48c4d41c1fbc32b57b9fa036e/src) and the Go project's [Code Review Comments](https://go.dev/wiki/CodeReviewComments). These are composition exemplars; the skill's documented authority order remains controlling.

Representative packages include `bytes`, `io`, `archive/zip`, `net/http`, `os`, `sync`, and `slices`. Prefer recurring patterns across several handwritten packages over a single file's historical or performance-driven choice.

## GO-STD-001: Start from a compact package vocabulary

Write the package's purpose as one clear sentence, then design the smallest exported set of nouns and verbs that fulfills it. Let the package name carry context, keep implementation details unexported, and make the common call sequence readable before adding convenience APIs.

Keep related behavior in one package when it shares invariants or unexported representation. Create a subpackage only for an independently nameable responsibility with its own callers; use `internal` when implementation must be shared without becoming a supported public import path. Do not copy the standard library's repository layout as a universal application skeleton.

## GO-STD-002: Make construction, zero values, and ownership deliberate

Prefer a useful zero value when it is safe and makes the type easier to compose. Add a constructor when callers must supply a dependency, establish an invariant, acquire a resource, or choose behavior that a zero value cannot express clearly. Return concrete types by default and keep mutable representation unexported unless fields are intentionally caller-configured API.

Document whether returned slices, readers, writers, handles, or views alias internal state; who closes resources; whether a value may be copied; and which operations are safe concurrently. Do not add Java-style getters, setters, factories, or builders around state that ordinary fields, methods, or a zero value already express clearly.

## GO-STD-003: Organize files and declarations as a reading path

Name and split files by coherent responsibility such as reading, writing, streaming, errors, or platform adaptation. Keep a primary type with its core behavior and place narrow helper state near the behavior it supports. Use standard filename suffixes and build constraints for platform-specific implementations, with a common platform-independent contract when practical.

Within a file, arrange declarations so a reader encounters the contract and primary behavior before incidental machinery. Group methods by lifecycle or behavior rather than alphabetically; place private helpers close enough to the invariant or operation they explain. There is no mandatory constructor position, declaration template, or one-type-per-file rule.

## GO-STD-004: Keep the implementation concrete and direct

Handle invalid inputs, terminal states, and errors early so the successful path stays shallow. Express the operation with ordinary control flow and standard interfaces, then extract an unexported helper only when it names a real invariant, isolates a repeated mechanism, or makes the main path easier to verify.

Use canonical operation names and short locals where a tight scope makes their role obvious; lengthen names as distance or ambiguity grows. Add an optional fast path only after the general path is correct and a canonical interface, compatibility need, or measurement justifies it. Do not generate service, manager, factory, adapter, or helper layers without a concrete boundary.

## GO-STD-005: Comment contracts and invariants

Use exported documentation to state behavior, ownership, aliasing, zero-value semantics, errors, and concurrency guarantees. Use internal comments for non-obvious invariants, arithmetic, protocol constraints, compatibility decisions, or deliberately unusual code. Avoid narrating control flow or commenting every private helper merely because it exists.

Keep runnable examples and focused tests beside the behavior they teach. Prefer tests that demonstrate the public call sequence and observable contract over tests coupled to declaration order or unexported representation.

## GO-STD-006: Do not imitate toolchain exceptions by default

Treat `runtime`, compiler, linker, assembler, generated tables, `unsafe`, `go:linkname`, bootstrap, and Go 1 compatibility machinery as specialized evidence. Adopt their patterns only when the target has the same low-level, performance, ABI, generation, or compatibility constraint and that choice still satisfies the higher-authority guidance.

Before emitting new code, verify this sequence: package promise, minimal exported API, zero-value and ownership story, responsibility-based files, coherent method groups, direct implementation, focused tests, then `gofmt` and repository checks.
