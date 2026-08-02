# Naming and Comments

Sources: [`decisions.md#naming`](https://github.com/google/styleguide/blob/gh-pages/go/decisions.md#naming), [`decisions.md#variable-names`](https://github.com/google/styleguide/blob/gh-pages/go/decisions.md#variable-names), [`decisions.md#repetition`](https://github.com/google/styleguide/blob/gh-pages/go/decisions.md#repetition), and [`best-practices.md#naming`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#naming).

## GO-NAME-001: Use idiomatic Go names

Use `MixedCaps` and `mixedCaps`, not underscores in ordinary identifiers. Keep names short when their scope is small and descriptive when their scope or lifetime is large. Avoid redundant package prefixes such as `http.HTTPClient` when `http.Client` is sufficient.

## GO-NAME-002: Preserve standard initialisms

Write common initialisms consistently: `ID`, `URL`, `HTTP`, `API`, `JSON`, `SQL`, and similar forms. Do not mix `Id`, `Url`, or `Http` into the same codebase without a strong local reason.

## GO-NAME-003: Name packages for what they provide

Use short, lowercase package names without underscores or generic suffixes such as `util`, `common`, or `helpers` when a domain-specific name is available. Avoid names likely to be shadowed by common locals, and avoid repeating the package name in exported identifiers. Keep imported package aliases consistent across nearby files.

## GO-NAME-004: Choose receiver names consistently

Use a short receiver name derived from the type, and use the same receiver name across the type's methods. Do not use `this` or `self` by default.

## GO-NAME-005: Match variable length to scope and use

Make a name longer as its scope and lifetime grow, and shorter when it is used repeatedly in a small, obvious block. As a rough, non-binding heuristic, a small scope is 1-7 lines, medium is 8-15, large is 15-25, and very large is beyond a page. A one- or two-letter name can be correct for a local counter, receiver, or familiar `io.Reader`/`io.Writer`; it is usually too vague for package state, a long function, or a scope with several similar values. Treat numeric scope ranges as heuristics, not limits.

## GO-NAME-006: Name what the value means in the current context

Start with a simple word such as `count` or `options`, then add words only to disambiguate (`userCount`, `projectCount`). Name the value being used, not the field, protocol, file, or function where it came from. Omit type words that the compiler and context already make clear (`users`, not `userSlice`; `name`, not `nameString`), except when representations coexist (`limitRaw` and `limit`). Do not shorten words merely to save typing; use a standard abbreviation or the full word.

## GO-NAME-007: Use single-letter names only when repetition is obvious

Use single-letter identifiers for conventional loop indices and coordinates, short-lived range values, and familiar receiver or stream names when the full name would be repetitive. Expand the name when the scope grows, the value's meaning is not conventional, or several similar values are in play.

## GO-NAME-008: Remove names that repeat their surrounding context

Package, type, method, function, import, and filename context already qualifies names. Prefer `reporting.Report` over `reporting.AdsTargetingRevenueReport`, `(*Project).Name` over `ProjectName`, and `db.Load` over `db.LoadFromDatabase` when the omitted words add no information. Apply this at the call site and keep names that prevent a real collision or ambiguity. There is no universal ban on names such as `Config`, `Client`, `Service`, or `Store`; change them only when the package-qualified name obscures the role or stutters without adding meaning.

## GO-NAME-009: Use constants for roles, not values

Name constants with `MixedCaps` like other identifiers, and describe the role the value plays (`MaxPacketSize`, not `512` or `Twelve`). Do not use all-caps, `k` prefixes, or value-derived names. Follow the repository's documented exceptions for generated or interoperability code.

## GO-NAME-010: Avoid accidental name shadowing

Do not introduce a local name that hides a package, parameter, outer variable, or important error value when that makes the active value difficult to identify. A short declaration is acceptable only when its scope and rebinding are obvious; otherwise choose a distinct name or a regular declaration.

## GO-NAME-011: Keep underscore exceptions explicit

Do not use underscores in ordinary Go identifiers. The narrow exceptions are generated-only package names, test/benchmark/example function or package names, and low-level OS or cgo interoperability. Filenames are not identifiers; imported generated packages should still receive an idiomatic local alias.

## GO-NAME-012: Avoid redundant `Get` prefixes

Name accessors after the value they expose (`Counts`, not `GetCounts`) unless the domain concept itself is a get operation, such as HTTP GET. Use a name such as `Compute` or `Fetch` when the call performs work or a remote operation so its cost and failure potential are visible.

## GO-NAME-013: Judge API names at the call site

Read exported declarations as callers see them: `package.Type`, `value.Method`, and `package.New(...)`. Prefer a noun for a value or type and a verb for an operation. Use `New` when package context makes the constructed type obvious; retain a qualified constructor such as `NewClient` when the package constructs several public types or `New` would be ambiguous. Keep method names specific enough to reveal meaningful work or side effects without repeating the receiver type.

Examples are contextual rather than automatic substitutions: `notion.New` may be clearer than `notion.NewStore` in a package centered on one store, while `image.NewDecoder` distinguishes one of several constructed types. A remote `client.FetchProgress` may communicate cost better than `client.Progress`, while a cheap field-like accessor should remain noun-like.

## GO-NAME-014: Name types for their role

Name a type for the role callers or maintainers reason about, not merely its fields or an incidental implementation detail. Domain values should use domain nouns (`Book`); transport representations may use a representation qualifier (`bookRecord`); work passed through a queue may use an execution role (`bookJob`). A structural name such as `indexedBook` is appropriate only when being indexed is the enduring abstraction rather than an implementation detail.

Choose among broad role names such as `Config`, `Settings`, `Options`, `Client`, `Service`, and `Store` by reading the package-qualified name and constructor call. Do not rename a coherent local convention merely to prefer one synonym.

## GO-COMMENT-001: Write doc comments for exported API

Start exported type, function, method, constant, and variable comments with the declared name. Explain behavior, ownership, units, nil semantics, error semantics, or constraints that callers need to know.

## GO-COMMENT-002: Comment intent, not syntax

Use comments to explain why a decision exists, what invariant must hold, or what external behavior constrains the code. Remove comments that merely restate the next line.

## GO-COMMENT-003: Keep comments complete and stable

Write comments as sentences when they are prose. Keep examples and comments synchronized with behavior. Do not leave stale deferred notes that no longer describe an actionable task.

## GO-COMMENT-004: Wrap comments for readers without a fixed width rule

There is no mandatory comment column. Wrap long prose when it improves reading in narrow tools, keep long literals or URLs intact when wrapping would make them less clear, and stay consistent within the file. Documentation comments should be complete, capitalized, and punctuated sentences; short field comments may be fragments.

## GO-DOC-003: Document package usage with runnable examples

Package comments should explain the package's purpose and intended use. Put runnable examples in `*_test.go` so they are compiled and rendered with the API documentation; use ordinary code comments only when a runnable example is not practical.
