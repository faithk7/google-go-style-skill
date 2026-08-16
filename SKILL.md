---
name: google-go-style
description: Apply Google's Go Style Guide, modern Effective Go idioms, and compatible Go standard-library composition when writing, refactoring, or reviewing Go code. Use when the user requests Google Go Style, Effective Go, idiomatic or standard-library-like Go, or focused guidance on naming, package or API boundaries, declaration or method organization, generated code, code generation, external contracts, dependency design, global state, formatting, comments, language mechanics, API design, errors, contexts, logging, interfaces, concurrency, documentation, testing, clarity, or maintainability; cite the bundled rules and distinguish requirements from preferences.
---

# Google Go Style

Use this skill to make Go code clear, simple, consistent, and maintainable while preserving the repository's existing behavior and explicit local conventions.

## Operating rules

- Inspect repository instructions, `go.mod`, package boundaries, and nearby code before choosing a pattern.
- Classify affected files as handwritten, generated, schema-derived, or constrained by an external interface before recommending style changes. Locate the authoritative generator, template, schema, or interface when one exists.
- When writing new code, shape the package contract and smallest useful API before filling in implementation. Use [`standard-library-style.md`](references/standard-library-style.md) to choose organization, naming, method layout, and implementation patterns only after higher-authority rules and local conventions are satisfied.
- Treat explicit repository-local instructions as overrides only where they are deliberate and documented. Read `AGENTS.md` and `.go-style.md` when present.
- Prefer the smallest mechanism that makes the behavior correct and obvious. Do not introduce abstractions, interfaces, helpers, or configuration only to satisfy a style preference.
- Resolve decisions in this order: correctness and API safety, clarity, simplicity, maintainability, consistency, then personal taste.
- Use `Must`, `Should`, and `May` precisely. Do not invent a universal rule where the upstream guide leaves room for judgment, especially around line length, package size, or interface placement.
- Use [`effective-go.md`](references/effective-go.md) for core language mechanics and established idioms. It is supplementary historical guidance, not a source for modern generics, modules, or newer APIs; prefer current Go documentation and the current Google baseline when they differ.
- Preserve runtime behavior, error semantics, and source compatibility during style refactors. Before renaming exported API, determine who can import it and call out any unavoidable source break before editing.
- Keep comments focused on intent, invariants, constraints, or non-obvious tradeoffs. Do not narrate syntax.
- When the user asks for detailed guidance, state the preferred choice, the signals that make it appropriate, important exceptions, and a compact example when it resolves ambiguity. Cite the applicable bundled rule and do not inflate a contextual recommendation into a requirement.

## Authority and conflicts

Resolve overlapping guidance in this order:

1. Go language semantics and the current Go specification or standard-library documentation.
2. Deliberate repository-local instructions, when they do not violate correctness, API safety, security, or resource ownership.
3. The current pinned Google Go Style Guide for modern style and API decisions.
4. [`effective-go.md`](references/effective-go.md) for historical core-language idioms and examples.
5. Personal preference.

Within the pinned Google baseline, use `guide.md` for principles, `decisions.md` for the normative style position, and `best-practices.md` for contextual techniques and tradeoffs. A Best Practices recommendation does not become a universal rule when its stated preconditions do not apply.

Treat Effective Go examples as explanatory, not as mandatory architecture. When an older example conflicts with current guidance, preserve the language semantics and apply the current Google rule. In particular, do not use historical `panic`/`recover`, initialization, error-prefix, or library examples to justify behavior that the current baseline rejects.

Use the pinned handwritten `golang/go` samples as a non-normative implementation exemplar after resolving the rules above. They help choose among otherwise valid designs; they do not override repository policy, the Google baseline, or documented exceptions. Do not imitate compiler, runtime, assembly, generated, `unsafe`, or compatibility-driven patterns without the same constraints.

## Focused requests

When the user names one or more style concerns, treat them as an explicit focus across writing, refactoring, and review:

1. Map the user's natural-language terms to the closest concerns in the focus map below. Combine references when the request names multiple concerns.
2. State the interpretation once in the initial work update when one is sent. Ask a question only when materially different interpretations would change the work. Repeat the focus in the final response only when it helps distinguish multiple concerns or formal review sections.
3. Load [`principles.md`](references/principles.md) plus only the selected topic references. In review mode, apply only the matching parts of [`review-checklist.md`](references/review-checklist.md).
4. Limit routine analysis, edits, and findings to the selected concerns. Run the checks needed to prove that the focused change preserves behavior.

If the user does not name a focus, do not announce one. Preserve the normal task-driven workflow and apply all guidance relevant to the request.

| User concern or common wording | Topic references | Interpretation |
| --- | --- | --- |
| File structure, package organization, package layout | [`packages-and-documentation.md`](references/packages-and-documentation.md), [`naming-and-comments.md`](references/naming-and-comments.md) | Assess file and package grouping through cohesion, ownership, boundaries, discoverability, and package names. Do not impose a universal `cmd/`, `internal/`, or `pkg/` layout. |
| Go standard-library style, `golang/go` style, declaration order, method organization, implementation shape, or writing a new package or type | [`standard-library-style.md`](references/standard-library-style.md), [`packages-and-documentation.md`](references/packages-and-documentation.md), [`naming-and-comments.md`](references/naming-and-comments.md), [`language-and-api-design.md`](references/language-and-api-design.md), [`formatting-and-imports.md`](references/formatting-and-imports.md) | Start from a compact package vocabulary, useful zero values and explicit ownership, responsibility-based files, coherent method groups, direct control flow, and `gofmt`-defined mechanics. Treat repository examples as compatible composition evidence rather than authority. |
| Generated code, code generation, generators, templates, schema or IDL output, generated markers, or external interface compatibility | [`generated-code-and-contracts.md`](references/generated-code-and-contracts.md), [`naming-and-comments.md`](references/naming-and-comments.md), [`testing.md`](references/testing.md) | Identify the authoritative edit point, preserve required contract names and wire shapes, keep generated exceptions from leaking into handwritten code, and validate regeneration rather than editing systematic output by hand. |
| Package or API boundaries, dependency direction, exported surface, global state, registries, dependency injection, or CLI/library separation | [`packages-and-documentation.md`](references/packages-and-documentation.md), [`interfaces-and-concurrency.md`](references/interfaces-and-concurrency.md), [`language-and-api-design.md`](references/language-and-api-design.md), [`common-libraries.md`](references/common-libraries.md) | Test cohesion from the caller and implementation perspectives, prefer explicit dependencies, justify exported interfaces and package state, and keep program wiring outside reusable libraries. |
| Variable, local, loop, parameter, receiver, package, test-double, or helper names; scope, abbreviations, shadowing, or repetition | [`naming-and-comments.md`](references/naming-and-comments.md), [`testing.md`](references/testing.md) | Apply scope-proportional names, conventional abbreviations and initialisms, contextual non-repetition, deliberate reassignment, receiver names, and behavior-based test-double names. |
| Function, method, constructor, accessor, type, struct, field, interface, or constant names; stutter or call-site readability | [`naming-and-comments.md`](references/naming-and-comments.md), [`packages-and-documentation.md`](references/packages-and-documentation.md), [`interfaces-and-concurrency.md`](references/interfaces-and-concurrency.md) | Judge the complete `package.Type`, `value.Method`, and constructor call; name domain, transport, and execution types by role; expose meaningful cost or side effects; and assess source compatibility before exported renames. |
| Formatting, imports, line wrapping, or literals | [`formatting-and-imports.md`](references/formatting-and-imports.md) | Apply mechanical formatting, import grouping, readability, and literal guidance. |
| Comments, doc comments, or documentation | [`naming-and-comments.md`](references/naming-and-comments.md), [`packages-and-documentation.md`](references/packages-and-documentation.md) | Cover intent comments, exported API documentation, configuration, lifecycle, concurrency, cleanup, rendered documentation, and proximity to code. |
| Errors, context, logging, cleanup, or cancellation | [`errors-context-and-logging.md`](references/errors-context-and-logging.md), [`interfaces-and-concurrency.md`](references/interfaces-and-concurrency.md) | Cover error ownership, context propagation, reporting, resources, cancellation, and completion. |
| Interfaces, concurrency, goroutines, channels, mutexes, or shared state | [`interfaces-and-concurrency.md`](references/interfaces-and-concurrency.md) | Cover interface ownership and size, goroutine lifetime, synchronization, zero values, and shared state. |
| Language mechanics, idioms, `defer`, allocation, slices, maps, initialization, embedding, conversions, or the blank identifier | [`effective-go.md`](references/effective-go.md), [`language-and-api-design.md`](references/language-and-api-design.md), [`interfaces-and-concurrency.md`](references/interfaces-and-concurrency.md) | Apply core-language behavior and idioms, while preferring current Go documentation and the current Google baseline for newer features. |
| API design, functions, arguments, option structs, functional options, result parameters, types, control flow, nil, pointers, or generics | [`language-and-api-design.md`](references/language-and-api-design.md), [`interfaces-and-concurrency.md`](references/interfaces-and-concurrency.md), [`packages-and-documentation.md`](references/packages-and-documentation.md), [`effective-go.md`](references/effective-go.md) | Cover call-site clarity, mechanism cost, language choices, and the caller-visible contract, loading only the references needed for the concrete API concern. |
| Flags, logging, contexts, or cryptographic randomness | [`common-libraries.md`](references/common-libraries.md), [`errors-context-and-logging.md`](references/errors-context-and-logging.md) | Apply the common-library decisions at program and API boundaries; preserve repository-specific logging and security conventions. |
| Tests, test cases, test doubles, test helpers, test packages, or integration transports | [`testing.md`](references/testing.md), [`naming-and-comments.md`](references/naming-and-comments.md) | Cover observable behavior, test structure, diagnostics, helper ownership, setup, package visibility, reusable doubles, and faithful component integration. |

Treat focus as a boundary, not merely a ranking signal. Still report a verified out-of-focus problem when it threatens correctness, API safety, data integrity, security, or resource and goroutine cleanup. Do not classify a general maintainability preference as critical outside the focus. For review, place such findings after the focused findings under `Out-of-focus critical findings`. For writing or refactoring, do not fix them unless the focused work cannot be completed safely without the smallest supporting change; otherwise report them separately.

Do not reinterpret performance, security, or architecture analysis as Go style. Apply any relevant style rules, state the boundary, and use or recommend the appropriate specialist when the request requires deeper analysis.

## Workflow

1. **Establish context.** Identify the requested behavior, affected packages, supported Go version, existing tests, local policies, source provenance, and any generator or external contract that owns the code shape.
2. **Resolve focus.** Identify explicit concerns, state the interpretation when useful, and keep concern focus distinct from the requested files or packages.
3. **Select references.** Start with [`principles.md`](references/principles.md), then load the focused or otherwise relevant topic files. For new packages, types, or substantial implementations, also load [`standard-library-style.md`](references/standard-library-style.md) unless the user set a narrower explicit focus that does not select standard-library composition.
4. **Implement or review.** Apply the rule IDs and decision tests in the selected references. Prefer standard library facilities and idiomatic control flow. Keep changes scoped to the request.
5. **Check the result.** Prefer the repository's aggregate check command when it subsumes formatting, vetting, and tests; otherwise run the applicable checks individually. For renames, search the repository for stale identifiers and inspect interface, generated, documentation, reflection, serialization, and configuration references. Do not rewrite files or add tooling without authorization.
6. **Explain decisions.** For non-obvious choices, cite the rule ID, identify the deciding signals, explain the tradeoff in plain language, and name a relevant exception when one exists.

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

For a generated finding, use the generator, template, schema, or IDL as `Location` when it is available and name the generated file as evidence. If the authoritative source is unavailable, say so and recommend changing it rather than directly patching repeatable output. Do not suppress correctness or security findings merely because the evidence is generated.

## Reference map

- [`principles.md`](references/principles.md): clarity, simplicity, concision, maintainability, and consistency.
- [`formatting-and-imports.md`](references/formatting-and-imports.md): `gofmt`, import grouping, line readability, and literal formatting.
- [`naming-and-comments.md`](references/naming-and-comments.md): names, initialisms, receivers, package names, doc comments, and commentary.
- [`errors-context-and-logging.md`](references/errors-context-and-logging.md): error flow, wrapping, strings, context propagation, and logging.
- [`interfaces-and-concurrency.md`](references/interfaces-and-concurrency.md): interface ownership, zero values, goroutine lifetimes, channels, and cancellation.
- [`language-and-api-design.md`](references/language-and-api-design.md): literals, receivers, copying, panic policy, generics, and function arguments.
- [`standard-library-style.md`](references/standard-library-style.md): compatible `golang/go` composition patterns for package surfaces, names, files, method groups, direct implementations, and comments.
- [`generated-code-and-contracts.md`](references/generated-code-and-contracts.md): generated-source provenance, external contracts, authoritative edit points, and regeneration checks.
- [`effective-go.md`](references/effective-go.md): core language mechanics and established idioms for formatting, names, control flow, functions, data structures, initialization, interfaces, embedding, concurrency, errors, and panic/recover.
- [`common-libraries.md`](references/common-libraries.md): flags, logging, and cryptographic randomness at program boundaries.
- [`packages-and-documentation.md`](references/packages-and-documentation.md): package boundaries, utility packages, public APIs, and documentation.
- [`testing.md`](references/testing.md): subtests, table-driven tests, helpers, test packages, and failure diagnostics.
- [`review-checklist.md`](references/review-checklist.md): a compact end-to-end review pass.
- [`extension-template.md`](references/extension-template.md): how to add project or team rules without changing the Google baseline.
- [`source-map.md`](references/source-map.md): upstream provenance, section mapping, and update policy.

## Boundaries

- Use this skill for Go source, tests, package design, and Go-facing documentation.
- Use a security, performance, or architecture specialist when the request requires analysis beyond style and maintainability.
- Do not automatically install linters, change `go.mod`, run destructive commands, or reformat unrelated files.
