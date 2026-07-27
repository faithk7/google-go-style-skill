# Errors, Context, and Logging

Sources: [`decisions.md`](https://github.com/google/styleguide/blob/gh-pages/go/decisions.md#errors) and [`best-practices.md`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#error-handling).

## GO-ERR-001: Keep error flow visible

Handle errors immediately at the operation that can provide useful context. Keep the success path readable and avoid deeply nested error branches. Never discard an error without a documented reason.

## GO-ERR-002: Add context at ownership boundaries

Wrap errors when crossing a package, operation, or user-visible boundary. Include the operation and relevant stable identifier, and preserve the cause with `%w` when callers may need `errors.Is` or `errors.As`.

## GO-ERR-003: Keep error strings machine-neutral

Use lowercase error strings without punctuation or redundant prefixes. Put structured context in wrapping fields or logs, not in an error string that callers must parse.

## GO-ERR-004: Separate handling from reporting

Handle an error where the program can recover or choose a policy. Log it at the boundary that owns reporting. Avoid logging and returning the same error repeatedly unless the layers add distinct actionable context.

## GO-CTX-001: Propagate context explicitly

Accept `context.Context` as the first parameter for work that can block, wait, access a remote service, or be cancelled. Pass the caller's context through rather than storing it on a long-lived struct or using a background context to hide ownership.

## GO-CTX-002: Make cancellation and cleanup observable

Use timeouts and cancellation at the boundary that owns the operation. Ensure goroutines, timers, response bodies, files, and other resources have a clear cleanup path.

## GO-LOG-001: Log actionable facts, not secrets

Use the repository's structured logging convention. Include operation, stable identifiers, and relevant outcomes; never log credentials, tokens, authorization headers, or sensitive payloads.
