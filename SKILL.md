---
name: google-go-style
description: Apply Google's Go Style Guide principles when writing, refactoring, or reviewing Go code, either comprehensively or with a natural-language focus. Use for focused or general work on package organization, naming, formatting, comments, API design, errors, context, logging, interfaces, concurrency, documentation, testing, and maintainability; cite the bundled rule references and distinguish correctness issues from style preferences.
---

# Google Go Style

Use this skill to make Go code clear, simple, consistent, and maintainable while preserving the repository's existing behavior and explicit local conventions.

## Operating rules

- Inspect repository instructions, `go.mod`, package boundaries, and nearby code before choosing a pattern.
- Treat explicit repository-local instructions as overrides only where they are deliberate and documented. Read `AGENTS.md` and `.go-style.md` when present.
- Prefer the smallest mechanism that makes the behavior correct and obvious. Do not introduce abstractions, interfaces, helpers, or configuration only to satisfy a style preference.
- Resolve decisions in this order: correctness and API safety, clarity, simplicity, maintainability, consistency, then personal taste.
- Use `Must`, `Should`, and `May` precisely. Do not invent a universal rule where the upstream guide leaves room for judgment, especially around line length, package size, or interface placement.
- Preserve public behavior and error semantics during style refactors. Call out any unavoidable behavior change before making it.
- Keep comments focused on intent, invariants, constraints, or non-obvious tradeoffs. Do not narrate syntax.

## Focused requests

When the user names one or more style concerns, treat them as an explicit focus across writing, refactoring, and review:

1. Map the user's natural-language terms to the closest concerns in the focus map below. Combine references when the request names multiple concerns.
2. Confirm the interpretation before acting and keep the final response self-contained. Use `Focus: <concern(s)>.` in the initial work update when one is sent, and begin the final response with the same line. Keep the wording recognizable to the user.
3. Load [`principles.md`](references/principles.md) plus only the selected topic references. In review mode, apply only the matching parts of [`review-checklist.md`](references/review-checklist.md).
4. Limit routine analysis, edits, and findings to the selected concerns. Run the checks needed to prove that the focused change preserves behavior.

If the user does not name a focus, do not announce one. Preserve the normal task-driven workflow and apply all guidance relevant to the request.

| User concern or common wording | Topic references | Interpretation |
| --- | --- | --- |
| File structure, package organization, package layout | [`packages-and-documentation.md`](references/packages-and-documentation.md), [`naming-and-comments.md`](references/naming-and-comments.md) | Assess file and package grouping through cohesion, ownership, boundaries, discoverability, and package names. Do not impose a universal `cmd/`, `internal/`, or `pkg/` layout. |
| Variable, identifier, receiver, or package names | [`naming-and-comments.md`](references/naming-and-comments.md) | Apply idiomatic naming, initialism, scope, receiver, and package-name guidance. |
| Formatting, imports, line wrapping, or literals | [`formatting-and-imports.md`](references/formatting-and-imports.md) | Apply mechanical formatting, import grouping, readability, and literal guidance. |
| Comments, doc comments, or documentation | [`naming-and-comments.md`](references/naming-and-comments.md), [`packages-and-documentation.md`](references/packages-and-documentation.md) | Cover intent comments, exported API documentation, configuration, lifecycle, and proximity to code. |
| Errors, context, logging, cleanup, or cancellation | [`errors-context-and-logging.md`](references/errors-context-and-logging.md), [`interfaces-and-concurrency.md`](references/interfaces-and-concurrency.md) | Cover error ownership, context propagation, reporting, resources, cancellation, and completion. |
| Interfaces, concurrency, goroutines, channels, mutexes, or shared state | [`interfaces-and-concurrency.md`](references/interfaces-and-concurrency.md) | Cover interface ownership and size, goroutine lifetime, synchronization, zero values, and shared state. |
| API design, functions, arguments, types, control flow, nil, pointers, or generics | [`language-and-api-design.md`](references/language-and-api-design.md), [`interfaces-and-concurrency.md`](references/interfaces-and-concurrency.md), [`packages-and-documentation.md`](references/packages-and-documentation.md) | Cover language choices and the caller-visible contract, loading only the references needed for the concrete API concern. |
| Tests, test cases, test helpers, or test packages | [`testing.md`](references/testing.md) | Cover observable behavior, test structure, diagnostics, helpers, setup, and package visibility. |

Treat focus as a boundary, not merely a ranking signal. Still report a verified out-of-focus problem when it threatens correctness, API safety, data integrity, security, or resource and goroutine cleanup. Do not classify a general maintainability preference as critical outside the focus. For review, place such findings after the focused findings under `Out-of-focus critical findings`. For writing or refactoring, do not fix them unless the focused work cannot be completed safely without the smallest supporting change; otherwise report them separately.

Do not reinterpret performance, security, or architecture analysis as Go style. Apply any relevant style rules, state the boundary, and use or recommend the appropriate specialist when the request requires deeper analysis.

## Workflow

1. **Establish context.** Identify the requested behavior, affected packages, supported Go version, existing tests, and local policies.
2. **Resolve focus.** Identify explicit concerns, confirm them when present, and keep concern focus distinct from the requested files or packages.
3. **Select references.** Start with [`principles.md`](references/principles.md), then load the focused or otherwise relevant topic files.
4. **Implement or review.** Apply the rule IDs in the selected references. Prefer standard library facilities and idiomatic control flow. Keep changes scoped to the request.
5. **Check the result.** Run the repository's normal checks when available. At minimum, consider `gofmt -l`, `go vet ./...`, and `go test ./...`; do not rewrite files or add tooling without authorization.
6. **Explain decisions.** For non-obvious choices, cite the rule ID and explain the tradeoff in plain language.

## Review mode

When reviewing code, report focused findings before any out-of-focus critical findings and the summary. For each finding include:

```text
[P1] GO-ERR-003 — short title
Location: path/to/file.go:line
Impact: concrete correctness, maintenance, or readability consequence
Recommendation: smallest safe change
Source: references/errors-context-and-logging.md#...
```

Use `P0` for a blocking correctness or safety issue, `P1` for a significant defect or maintainability risk, `P2` for a localized improvement, and `P3` for polish. Do not report a preference as a defect; state when an observation is optional. Mention positive patterns and test gaps after the findings.

## Reference map

- [`principles.md`](references/principles.md): clarity, simplicity, concision, maintainability, and consistency.
- [`formatting-and-imports.md`](references/formatting-and-imports.md): `gofmt`, import grouping, line readability, and literal formatting.
- [`naming-and-comments.md`](references/naming-and-comments.md): names, initialisms, receivers, package names, doc comments, and commentary.
- [`errors-context-and-logging.md`](references/errors-context-and-logging.md): error flow, wrapping, strings, context propagation, and logging.
- [`interfaces-and-concurrency.md`](references/interfaces-and-concurrency.md): interface ownership, zero values, goroutine lifetimes, channels, and cancellation.
- [`language-and-api-design.md`](references/language-and-api-design.md): literals, receivers, copying, panic policy, generics, and function arguments.
- [`packages-and-documentation.md`](references/packages-and-documentation.md): package boundaries, utility packages, public APIs, and documentation.
- [`testing.md`](references/testing.md): subtests, table-driven tests, helpers, test packages, and failure diagnostics.
- [`review-checklist.md`](references/review-checklist.md): a compact end-to-end review pass.
- [`extension-template.md`](references/extension-template.md): how to add project or team rules without changing the Google baseline.
- [`source-map.md`](references/source-map.md): upstream provenance, section mapping, and update policy.

## Boundaries

- Use this skill for Go source, tests, package design, and Go-facing documentation.
- Use a security, performance, or architecture specialist when the request requires analysis beyond style and maintainability.
- Do not automatically install linters, change `go.mod`, run destructive commands, or reformat unrelated files.
