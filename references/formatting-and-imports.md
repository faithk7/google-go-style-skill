# Formatting and Imports

Sources: [`guide.md`](https://github.com/google/styleguide/blob/gh-pages/go/guide.md#core-guidelines), [`decisions.md`](https://github.com/google/styleguide/blob/gh-pages/go/decisions.md#imports), and [`best-practices.md`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#imports).

## GO-FMT-001: Let `gofmt` define mechanical formatting

Run `gofmt` on changed Go files. Do not hand-format code in a way that fights the formatter. Keep formatting-only changes separate from behavioral changes when that improves reviewability.

## GO-FMT-002: Keep import groups meaningful

Use standard-library imports first, followed by a blank line and non-standard imports. Preserve project-specific grouping conventions when they are deliberate. Avoid dot imports; rename an import only to resolve a collision or make a necessary distinction clear.

When the repository uses the Google grouping convention, keep generated protocol-buffer imports and side-effect-only imports in their own groups after ordinary project imports. Rename an import consistently when a collision or an uninformative package name requires it.

## GO-FMT-003: Do not enforce an arbitrary line limit

Break long lines when doing so improves scanning, nesting, or diffs. Do not introduce awkward wrapping solely to satisfy a numeric width rule. Keep comments and literals readable and avoid horizontal complexity.

In particular, keep function and method signatures on one line when possible, avoid line breaks in `if` clauses that look like block indentation, and extract well-named local values when a condition is too complex to scan.

## GO-FMT-004: Make composite literals unambiguous

Use field names in struct literals, especially across package boundaries or when a type has multiple similar fields. Omit redundant type names only when the surrounding literal remains obvious.

## GO-FMT-005: Keep formatting changes scoped

Do not reformat unrelated packages during a focused change. If the repository has a formatter or generated-code convention, follow it rather than creating a second style.

## GO-FMT-006: Make diagnostic strings unambiguous

Use `%q` for human-facing strings that may be empty or contain control characters instead of manually adding quotes. Use the repository's established formatting and logging conventions for other values.
