# Errors, Context, and Logging

Sources: [`decisions.md#errors`](https://github.com/google/styleguide/blob/gh-pages/go/decisions.md#errors), [`best-practices.md#error-handling`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#error-handling), and [`best-practices.md#documentation-conventions-errors`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#documentation-conventions-errors).

## GO-ERR-001: Keep error flow visible

Handle errors immediately at the operation that can provide useful context. Keep the success path readable and avoid deeply nested error branches. Never discard an error without a documented reason.

## GO-ERR-005: Return errors as the final result with a clear contract

Use the `error` interface as the final result for operations that can fail, and return `nil` on success. Unless documented otherwise, callers must treat other results as unspecified when `err != nil`; exported functions should not expose a concrete error pointer as their error result.

## GO-ERR-006: Prefer explicit errors over in-band sentinel values

Do not use values such as `-1`, `nil`, or an empty string to signal failure when a second result can express the condition. Return an `error` when callers need an explanation, or a final boolean such as `ok` when they only need presence or absence.

## GO-ERR-007: Discard an error only with a local proof

Do not assign errors to `_` by habit. If an operation is documented to be unable to fail or its failure is intentionally irrelevant, keep the discard local and comment why it is safe.

## GO-ERR-002: Add context at ownership boundaries

Add information when crossing a package, operation, or user-visible boundary only if it explains what the current layer was trying to accomplish. Include a stable operation or identifier, but do not repeat a path, resource, or failure already present in the underlying error. If the only added word is `failed`, return the original error.

## GO-ERR-008: Preserve or translate error identity deliberately

Use `%w` when callers should inspect the original identity with `errors.Is` or `errors.As`, and document stable sentinel or typed errors that form part of an exported contract. Use `%v`, a canonical status, or a domain error when crossing RPC, IPC, storage, security, or other abstraction boundaries where exposing the implementation error would couple callers to internals. Do not wrap automatically: decide which observers need human context and which need machine-readable identity.

## GO-ERR-009: Make error text follow the error chain

For ordinary contextual wrapping, put `%w` at the end in the form `"operation details: %w"` so printed text proceeds from newest context to oldest cause. A primary sentinel category may appear first as `"%w: details"` when surfacing the category early improves readability. Keep this exception deliberate; avoid placing a wrapped cause mid-sentence or mixing multiple layers into an order that no longer mirrors the chain.

## GO-ERR-003: Keep error strings machine-neutral

Use lowercase error strings without punctuation or redundant prefixes. Put structured context in wrapping fields or logs, not in an error string that callers must parse.

Effective Go's historical examples sometimes prefix an error string with its origin. Do not add such a prefix automatically: preserve an established public format when compatibility requires it, but otherwise identify the operation through `%w`, structured error data, or the reporting boundary.

## GO-ERR-004: Separate handling from reporting

Handle an error where the program can recover or choose a policy. Log it at the boundary that owns reporting. Avoid logging and returning the same error repeatedly unless the layers add distinct actionable context.

## GO-CTX-001: Propagate context explicitly

Accept `context.Context` as the first parameter for work that can block, wait, access a remote service, or be cancelled. Pass the caller's context through rather than storing it on a long-lived struct or using a background context to hide ownership.

The first-parameter convention does not require duplicating a context already provided by an HTTP request or streaming RPC; use the request or stream's context directly in those handlers.

## GO-CTX-002: Make cancellation and cleanup observable

Use timeouts and cancellation at the boundary that owns the operation. Ensure goroutines, timers, response bodies, files, and other resources have a clear cleanup path.

## GO-LOG-001: Log actionable facts, not secrets

Use the repository's structured logging convention. Include operation, stable identifiers, and relevant outcomes; never log credentials, tokens, authorization headers, or sensitive payloads.

Prefer a non-formatting logging call when no formatting is needed, and understand whether the repository's fatal or exit helper runs deferred cleanup before using it.
