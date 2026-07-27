# Packages and Documentation

Source: [`best-practices.md`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#package-size).

## GO-PKG-001: Keep package boundaries purposeful

Group code by a cohesive domain or responsibility. Avoid both giant packages with unrelated behavior and tiny packages that only move a few lines across an artificial boundary.

## GO-PKG-002: Keep utility packages rare

Place helpers near the domain that owns their meaning. A generic utility package is justified only when the abstraction is cohesive, broadly reusable, and named for its actual domain.

## GO-PKG-003: Keep APIs discoverable

Use exported names that read naturally at the call site. Keep internal details unexported unless callers need them. Make ownership, lifecycle, units, and error behavior visible in types or documentation.

## GO-DOC-001: Document configuration and lifecycle

Document required setup, defaults, valid ranges, cancellation, cleanup, retry behavior, and side effects. Treat configuration and operational behavior as part of the API.

## GO-DOC-002: Keep documentation close to code

Update package and exported API comments with the implementation. Prefer examples that compile or are covered by tests when the behavior is subtle.
