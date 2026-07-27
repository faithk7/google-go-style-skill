# Testing

Sources: [`decisions.md`](https://github.com/google/styleguide/blob/gh-pages/go/decisions.md#test-structure) and [`best-practices.md`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#tests).

## GO-TEST-001: Test behavior and error semantics

Cover the public behavior, boundary conditions, cancellation, and meaningful error identity or context. Do not increase coverage by asserting implementation details that callers cannot observe.

## GO-TEST-002: Use table-driven tests when cases share structure

Use named test rows and subtests for related inputs. Keep each row's setup, action, and want values explicit enough that a failure identifies the scenario.

## GO-TEST-003: Make failures diagnostic

Identify the function, input, got value, and want value. Use stable comparisons or diffs for structured results. Continue independent rows when doing so produces more useful feedback.

## GO-TEST-004: Keep helpers honest

Mark test helpers with `t.Helper()`. Do not call `t.Fatal` from a goroutine that does not own the test; return the failure to the test goroutine or use an assertion that is safe for the execution model.

## GO-TEST-005: Scope setup to the test that needs it

Avoid expensive package-wide initialization. Use `TestMain` only for setup that genuinely applies to every test and has a clear cleanup path.

## GO-TEST-006: Choose test package visibility deliberately

Use same-package tests when private behavior is part of the package's direct contract or needs close unit coverage. Use an external test package when testing only the public API or avoiding implementation coupling.
