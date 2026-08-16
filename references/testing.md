# Testing

Sources: [`decisions.md`](https://github.com/google/styleguide/blob/gh-pages/go/decisions.md#test-structure) and [`best-practices.md`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#tests).

## GO-TEST-001: Test behavior and error semantics

Cover the public behavior, boundary conditions, cancellation, and meaningful error identity or context. Do not increase coverage by asserting implementation details that callers cannot observe.

When behavior varies by operating system or architecture, exercise the affected filename suffixes, build constraints, and target compilation. Do not require a full platform matrix for an unrelated change; select the targets that can observe the behavior.

## GO-TEST-002: Use table-driven tests when cases share structure

Use named test rows and subtests for related inputs. Keep each row's setup, action, and want values explicit enough that a failure identifies the scenario. Split tests when rows require substantially different control flow instead of building a conditional mini-framework inside one table.

## GO-TEST-003: Make failures diagnostic

Identify the function, input, got value, and want value. Use stable comparisons or diffs for structured results. Continue independent rows when doing so produces more useful feedback.

## GO-TEST-004: Keep helpers honest

Use helpers for setup, cleanup, or reusable operations rather than hiding domain assertions. Mark a helper with `t.Helper()` when it can report a failure, use `t.Cleanup` for owned cleanup, and allow `t.Fatal` only when a failed setup precondition makes the current test or subtest impossible to run. A helper that cannot fail does not need `testing.T`.

Do not call `t.Fatal`, `t.FailNow`, or related methods from a goroutine that does not own the test. Return or send the failure to the test goroutine, or use `t.Error` where concurrent reporting is safe and then stop that goroutine's work.

## GO-TEST-005: Scope setup to the test that needs it

Avoid expensive package-wide initialization. Use `TestMain` only for setup that genuinely applies to every test and has a clear cleanup path.

## GO-TEST-006: Choose test package visibility deliberately

Use same-package tests when private behavior is part of the package's direct contract or needs close unit coverage. Use an external test package when testing only the public API or avoiding implementation coupling.

## GO-TEST-007: Make every failure identify the failed operation

Include the function, relevant input, actual (`got`) value, and expected (`want`) value in a failure. Name complex interactions or cases in the message rather than relying only on the test function name.

## GO-TEST-008: Compare stable semantics, not incidental representation

Compare complete structures with the repository's approved semantic comparison or diff tool instead of hand-checking fields. Avoid asserting byte or string formatting that belongs to a dependency you do not control; test parsed or semantic results instead, and label diff direction clearly.

## GO-TEST-009: Keep independent checks running

Use `t.Error` for independent mismatches so one failure does not hide the next. Use `t.Fatal` only when setup failed or continuing would make later results meaningless; never call fatal methods from a goroutine that does not own the test.

## GO-TEST-010: Keep subtests independent and filterable

Make subtest names concise, descriptive, and safe for `go test -run` filtering; avoid slashes and other characters with special filter meaning. Each subtest should establish its own required state and should be runnable without depending on another row's execution order.

## GO-TEST-011: Do not build assertion libraries

Use the standard `testing` package and write the comparison in the test's domain context. Keep simple repeated checks inline or unify similar cases in a table. When several tests need complex validation, write a helper that returns a value, `error`, or comparison option and let each `Test` function decide how to fail and which diagnostic context matters. Do not hide control flow behind a generic assertion DSL.

An existing assertion dependency is evidence of a local convention, not a change to the Google baseline. Do not perform an unrelated mass conversion solely for style. When a deliberate repository policy requires that dependency, follow it while keeping control flow, failure context, and the distinction between setup failures and independent mismatches visible.

## GO-TEST-012: Test error semantics, not wording

When the contract is error identity or category, use `errors.Is`, `errors.As`, or an approved semantic comparison. Compare error text only for documented user-facing properties, not as a proxy for the error type.

## GO-TEST-013: Exercise real integration boundaries when practical

For HTTP, RPC, and similar component integrations, prefer the production client and real in-process transport connected to a test server or fake backend. This exercises serialization, middleware, cancellation, and generated client behavior that a hand-written client double can miss. Use a narrower double when the real transport is unavailable, prohibitively expensive, nondeterministic, or outside the behavior under test, and explain that boundary in the test design.
