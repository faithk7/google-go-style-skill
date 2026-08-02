# Review Checklist

Use this checklist after reading the relevant topic reference. Report verified problems before optional suggestions.

## Correctness and behavior

- Does the change preserve the requested runtime behavior, error semantics, and supported public API?
- If an exported declaration changes, is the source-compatibility impact known and explicitly authorized?
- Are language semantics based on the current Go specification or standard-library documentation rather than an outdated example?
- When guidance overlaps, were repository rules, the current Google baseline, and Effective Go applied in the documented authority order?
- Are errors handled at the right ownership boundary and wrapped with useful context?
- Can cancellation, cleanup, and goroutine completion be proven?
- Are nil, zero, empty, timeout, retry, and partial-failure cases explicit?

## Clarity and maintainability

- Can a reader explain what and why the code does without reconstructing hidden state?
- Is the abstraction justified by a current caller or requirement?
- Do package, type, constructor, function, method, parameter, receiver, and initialism names read naturally at their call sites without hiding meaningful cost or side effects?
- Are exported APIs and operational side effects documented?

## Naming

- Is each variable's length proportional to its scope and lifetime, with longer names where similar values or distant uses need the reminder?
- Does each local name describe the value's current meaning rather than its source, type, or surrounding package/type context?
- Are single-letter names limited to conventional receivers, short loops, coordinates, or familiar stream variables?
- Are names free of accidental shadowing and unnecessary package, type, or value repetition?
- Are constants named for their role, package aliases consistent, and underscore exceptions limited to generated, test, or interoperability code?
- Do struct and other type names describe a stable domain, representation, or execution role rather than incidental fields or implementation details?

## Rename safety

- Is the declaration unexported, confined to an `internal` package, or part of an API consumed outside the repository?
- Were interface implementations, generated code and mocks, tests, examples, documentation, scripts, configuration, reflection strings, and serialization or schema names checked where relevant?
- Does a repository-wide search account for every reference to the old name, with any retained compatibility name or external-format string treated deliberately?
- If compatibility is required, was the smallest migration mechanism chosen without adding an alias or deprecated wrapper automatically?

## Core language idioms

- Are short declarations, variable scope, and shadowing clear?
- Is `defer` scoped to the resource owner, without retaining resources across an unbounded loop?
- Are `new`, `make`, composite literals, slices, `append`, nil maps, and comma-ok lookups used with their actual language semantics?
- Are receiver choices, embedding, type assertions, and blank-identifier uses intentional and visible at the API boundary?
- Do one-method interfaces and canonical methods use established names and signatures?
- Are channel closure, goroutine ownership, panic, and recover constrained to an explicit protocol or boundary?

## Common libraries

- Are flags defined only at the program boundary and kept out of reusable package APIs?
- Does security-sensitive randomness use `crypto/rand`, and does logging follow the repository's severity and cleanup semantics?

## Testing

- Do tests cover observable behavior and error semantics?
- Are cases named and failures diagnostic?
- Are test helpers safe for their goroutine and marked with `t.Helper()`?
- Is setup scoped and cleanup deterministic?

## Mechanical checks

- Prefer the repository's aggregate check command when it already covers formatting, vetting, and tests; do not repeat equivalent commands without a reason.
- Otherwise, run `gofmt -l` for changed Go files, `go vet ./...` when dependencies are available, and the relevant tests (normally `go test ./...`).
- For renames, search for stale identifiers across source, tests, generated inputs, documentation, and configuration.
- Review the diff for unrelated formatting, generated files, credentials, or new dependencies.
