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
