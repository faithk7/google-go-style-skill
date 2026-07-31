# Review Checklist

Use this checklist after reading the relevant topic reference. Report verified problems before optional suggestions.

## Correctness and behavior

- Does the change preserve the requested behavior and public API?
- Are errors handled at the right ownership boundary and wrapped with useful context?
- Can cancellation, cleanup, and goroutine completion be proven?
- Are nil, zero, empty, timeout, retry, and partial-failure cases explicit?

## Clarity and maintainability

- Can a reader explain what and why the code does without reconstructing hidden state?
- Is the abstraction justified by a current caller or requirement?
- Are package, type, function, parameter, receiver, and initialism names idiomatic and non-redundant?
- Are exported APIs and operational side effects documented?

## Naming

- Is each variable's length proportional to its scope and lifetime, with longer names where similar values or distant uses need the reminder?
- Does each local name describe the value's current meaning rather than its source, type, or surrounding package/type context?
- Are single-letter names limited to conventional receivers, short loops, coordinates, or familiar stream variables?
- Are names free of accidental shadowing and unnecessary package, type, or value repetition?
- Are constants named for their role, package aliases consistent, and underscore exceptions limited to generated, test, or interoperability code?

## Core language idioms

- Are short declarations, variable scope, and shadowing clear?
- Is `defer` scoped to the resource owner, without retaining resources across an unbounded loop?
- Are `new`, `make`, composite literals, slices, `append`, nil maps, and comma-ok lookups used with their actual language semantics?
- Are receiver choices, embedding, type assertions, and blank-identifier uses intentional and visible at the API boundary?
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

- Run `gofmt -l` for changed Go files.
- Run `go vet ./...` when the module and dependencies are available.
- Run the repository's test command, normally `go test ./...`.
- Review the diff for unrelated formatting, generated files, credentials, or new dependencies.
