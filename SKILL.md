---
name: google-go-style
description: Apply Google's Go Style Guide principles when writing, refactoring, or reviewing Go code. Use for Go naming, formatting, comments, package/API design, errors, context, logging, interfaces, concurrency, documentation, testing, and maintainability decisions; cite the bundled rule references and distinguish correctness issues from style preferences.
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

## Workflow

1. **Establish context.** Identify the requested behavior, affected packages, supported Go version, existing tests, and local policies.
2. **Select references.** Load only the relevant files from [`references/`](references/source-map.md). Start with [`principles.md`](references/principles.md), then follow the topic map.
3. **Implement or review.** Apply the rule IDs in the selected references. Prefer standard library facilities and idiomatic control flow. Keep changes scoped to the request.
4. **Check the result.** Run the repository's normal checks when available. At minimum, consider `gofmt -l`, `go vet ./...`, and `go test ./...`; do not rewrite files or add tooling without authorization.
5. **Explain decisions.** For non-obvious choices, cite the rule ID and explain the tradeoff in plain language.

## Review mode

When reviewing code, report findings before the summary. For each finding include:

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
