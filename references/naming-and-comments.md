# Naming and Comments

Sources: [`decisions.md`](https://github.com/google/styleguide/blob/gh-pages/go/decisions.md#naming) and [`best-practices.md`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#naming).

## GO-NAME-001: Use idiomatic Go names

Use `MixedCaps` and `mixedCaps`, not underscores in ordinary identifiers. Keep names short when their scope is small and descriptive when their scope or lifetime is large. Avoid redundant package prefixes such as `http.HTTPClient` when `http.Client` is sufficient.

## GO-NAME-002: Preserve standard initialisms

Write common initialisms consistently: `ID`, `URL`, `HTTP`, `API`, `JSON`, `SQL`, and similar forms. Do not mix `Id`, `Url`, or `Http` into the same codebase without a strong local reason.

## GO-NAME-003: Name packages for what they provide

Use short, lowercase package names without underscores or generic suffixes such as `util`, `common`, or `helpers` when a domain-specific name is available. Avoid repeating the package name in exported identifiers.

## GO-NAME-004: Choose receiver names consistently

Use a short receiver name derived from the type, and use the same receiver name across the type's methods. Do not use `this` or `self` by default.

## GO-COMMENT-001: Write doc comments for exported API

Start exported type, function, method, constant, and variable comments with the declared name. Explain behavior, ownership, units, nil semantics, error semantics, or constraints that callers need to know.

## GO-COMMENT-002: Comment intent, not syntax

Use comments to explain why a decision exists, what invariant must hold, or what external behavior constrains the code. Remove comments that merely restate the next line.

## GO-COMMENT-003: Keep comments complete and stable

Write comments as sentences when they are prose. Keep examples and comments synchronized with behavior. Do not leave stale deferred notes that no longer describe an actionable task.
