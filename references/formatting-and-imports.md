# Formatting and Imports

Sources: [`guide.md`](https://github.com/google/styleguide/blob/gh-pages/go/guide.md#core-guidelines), [`decisions.md`](https://github.com/google/styleguide/blob/gh-pages/go/decisions.md#imports), and [`best-practices.md`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#imports).

## GO-FMT-001: Let `gofmt` define mechanical formatting

Run `gofmt` on changed Go files. Do not hand-format code in a way that fights the formatter. Keep formatting-only changes separate from behavioral changes when that improves reviewability.

## GO-FMT-002: Keep import groups meaningful

Use standard-library imports first, followed by a blank line and non-standard imports. Preserve project-specific grouping conventions when they are deliberate. Avoid dot imports; rename an import only to resolve a collision or make a necessary distinction clear.

## GO-FMT-003: Do not enforce an arbitrary line limit

Break long lines when doing so improves scanning, nesting, or diffs. Do not introduce awkward wrapping solely to satisfy a numeric width rule. Keep comments and literals readable and avoid horizontal complexity.

## GO-FMT-004: Make composite literals unambiguous

Use field names in struct literals, especially across package boundaries or when a type has multiple similar fields. Omit redundant type names only when the surrounding literal remains obvious.

## GO-FMT-005: Keep formatting changes scoped

Do not reformat unrelated packages during a focused change. If the repository has a formatter or generated-code convention, follow it rather than creating a second style.
