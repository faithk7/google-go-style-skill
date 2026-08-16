# Review Checklist

Use this checklist after reading the relevant topic reference. Report verified problems before optional suggestions.

## Correctness and behavior

- Does the change preserve the requested runtime behavior, error semantics, and supported public API?
- If an exported declaration changes, is the source-compatibility impact known and explicitly authorized?
- Are language semantics based on the current Go specification or standard-library documentation rather than an outdated example?
- When guidance overlaps, were repository rules, the current Google baseline, and Effective Go applied in the documented authority order?
- Are errors handled at the right ownership boundary, annotated without repetition, and either wrapped or translated according to the caller-visible contract?
- Can cancellation, cleanup, and goroutine completion be proven?
- Are nil, zero, empty, timeout, retry, and partial-failure cases explicit?

## Clarity and maintainability

- Can a reader explain what and why the code does without reconstructing hidden state?
- Is the abstraction justified by a current caller or requirement?
- For newly authored handwritten packages or types, does the code begin with a compact vocabulary and smallest useful exported API rather than scaffolding speculative layers?
- Do package, type, constructor, function, method, parameter, receiver, and initialism names read naturally at their call sites without hiding meaningful cost or side effects?
- Does a complex signature use ordinary parameters, an options struct, or functional options for a reason supported by its actual call patterns?
- Are exported APIs and operational side effects documented, with one discoverable package comment and `doc.go` used only when it improves navigation?

## Boundaries

- Would callers normally need both sides of a proposed package split, or would splitting force paired imports, exported plumbing, or an interface created only to avoid a cycle?
- Are types and their core behavior close to the responsibility that owns or uses them, without generic `types`, `models`, or one-type-per-file organization?
- Does each public import path express a stable package identity rather than incidental repository structure, with any path move treated as a compatibility change?
- Does an ordinary `package main` keep implementation details unexported and move genuinely reusable behavior behind an importable package API?
- Does each exported interface have a real consumer or protocol role, live with the right owner, and contain only the methods that role needs?
- Do stateful libraries expose isolated instances and explicit dependencies instead of process-wide registries, setters, replaceable clients, or hidden initialization order?
- Is CLI wiring kept at the program boundary, with reusable behavior available through ordinary Go APIs and the command's context propagated?

## Standard-library composition

- Is the zero-value behavior intentional, with a constructor used only when dependencies, invariants, resources, or required configuration justify it?
- Are files split by coherent responsibility and platform suffixes rather than type symmetry, framework layers, or a copied repository skeleton?
- Do declaration and method groups form a readable lifecycle or behavioral path, with private helpers near the invariants they support rather than alphabetized mechanically?
- Does the successful path use direct, shallow control flow, with optional fast paths or abstraction layers justified by an actual contract or evidence?
- Were compiler, runtime, assembly, generated, `unsafe`, bootstrap, and compatibility patterns rejected unless the target shares their constraints?

## Generated code and external contracts

- Is each affected file classified as handwritten, generated, schema-derived, or constrained by an external interface, with the authoritative edit point identified?
- Does the generated marker use Go's recognized form, or is a repository-specific header being treated only as a local convention?
- Are names and wire shapes required by an external contract preserved without spreading their exceptions into unconstrained handwritten code?
- Will a systematic fix be made in the generator, template, schema, or IDL and verified through regeneration rather than patched repeatedly in output files?

## Naming

- Is each variable's length proportional to its scope and lifetime, with longer names where similar values or distant uses need the reminder?
- Does each local name describe the value's current meaning rather than its source, type, or surrounding package/type context?
- Are single-letter names limited to conventional receivers, short loops, coordinates, or familiar stream variables?
- Are names free of accidental shadowing and unnecessary package, type, or value repetition?
- Where a nested block updates an outer value, is reassignment explicit rather than an accidental `:=` shadow?
- Are constants named for their role, package aliases consistent, and underscore exceptions limited to generated, test, or interoperability code?
- Do struct and other type names describe a stable domain, representation, or execution role rather than incidental fields or implementation details?
- Are reusable test doubles named from package context, doubled role, and behavior without exporting test support that has no external consumer?

## Rename safety

- Is the declaration unexported, confined to an `internal` package, or part of an API consumed outside the repository?
- Were interface implementations, generated code and mocks, tests, examples, documentation, scripts, configuration, reflection strings, and serialization or schema names checked where relevant?
- Does a repository-wide search account for every reference to the old name, with any retained compatibility name or external-format string treated deliberately?
- If compatibility is required, was the smallest migration mechanism chosen without adding an alias or deprecated wrapper automatically?

## Core language idioms

- Are short declarations, variable scope, and shadowing clear?
- Do declarations distinguish intentional zero values, known members, and evidence-based capacity hints?
- Is `defer` scoped to the resource owner, without retaining resources across an unbounded loop?
- Are `new`, `make`, composite literals, slices, `append`, nil maps, and comma-ok lookups used with their actual language semantics?
- Are receiver choices, embedding, type assertions, and blank-identifier uses intentional and visible at the API boundary?
- Do one-method interfaces and canonical methods use established names and signatures?
- Are channel closure, goroutine ownership, panic, and recover constrained to an explicit protocol or boundary?

## Common libraries

- Are flags defined only at the program boundary and kept out of reusable package APIs?
- Does security-sensitive randomness use `crypto/rand`, and does logging follow the repository's severity and cleanup semantics?
- Does the process entry point own final error rendering and exit policy while command handlers propagate their supplied context?

## Testing

- Do tests cover observable behavior and error semantics?
- Are cases named and failures diagnostic?
- Are test helpers safe for their goroutine and marked with `t.Helper()`?
- Do assertion decisions remain in the test, with shared validation returning values, errors, or comparison options?
- Do component tests use the production client and real in-process transport when that boundary is practical and relevant?
- Is setup scoped and cleanup deterministic?
- When platform-specific source or build constraints are affected, are the relevant target builds or tests included?

## Mechanical checks

- Prefer the repository's aggregate check command when it already covers formatting, vetting, and tests; do not repeat equivalent commands without a reason.
- Otherwise, run `gofmt -l` for changed Go files, `go vet ./...` when dependencies are available, and the relevant tests (normally `go test ./...`).
- For renames, search for stale identifiers across source, tests, generated inputs, documentation, and configuration.
- Review the diff for unrelated formatting, generated files, credentials, or new dependencies.
