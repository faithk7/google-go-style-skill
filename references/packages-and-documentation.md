# Packages and Documentation

Google sources: [`best-practices.md#util-packages`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#util-packages), [`best-practices.md#package-size`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#package-size), and [`best-practices.md#documentation`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#documentation). Supplementary context: [Style guideline for Go packages](https://rakyll.org/style-packages/).

## GO-PKG-001: Keep package boundaries purposeful

Group code by a cohesive domain or responsibility. Keep concepts together when callers almost always need both to do useful work or when their implementations need shared unexported details; splitting them would force paired imports, exported plumbing, or circular dependencies. Split a concept when it has an independent purpose, ownership, lifecycle, or client population and can stand alone behind a clear package name.

Do not decide from line or type counts. A small cohesive package and a large multi-file domain can both be appropriate. Treat an interface introduced only to break an import cycle as a signal to recheck whether the packages were split along the wrong boundary.

## GO-PKG-002: Keep utility packages rare

Place helpers near the domain that owns their meaning. Judge the package name at the call site: `spannertest.NewDatabase`, `io.SeekStart`, and `elliptic.Marshal` convey ownership, while `util`, `common`, `helper`, or `model` usually hide it and invite import aliases. A shared package is justified only when its contents form a cohesive, broadly reusable domain that can be named for what it provides.

## GO-PKG-003: Keep APIs discoverable

Use exported names that read naturally at the call site. Keep internal details unexported unless callers need them. Make ownership, lifecycle, units, and error behavior visible in types or documentation.

## GO-PKG-004: Organize files for maintainers, not type symmetry

Group related declarations in files whose names make the implementation discoverable. Keep a type and its core behavior near the code that owns or uses it when this helps a maintainer find the concept without searching a generic `types.go` or `models` package. Split a very large file by subject when maintainers can predict where behavior lives, and combine tiny files when fragmentation makes navigation harder. Go has no one-type-per-file convention, and moving declarations within a package should not change its caller-visible API.

## GO-PKG-005: Keep public import paths intentional and stable

Choose module and subdirectory paths that communicate the package's domain rather than incidental repository storage. Avoid path segments such as `src`, `gosrc`, or repeated repository names when they exist only to mirror an internal layout and add no caller meaning. Do not require or ban `cmd`, `internal`, or `pkg` universally; use them only when their actual visibility or organization semantics fit the repository.

Treat a published import-path move as an API migration because Go identifies packages by import path. Check downstream consumers, module paths, generated code, documentation, and compatibility strategy before changing it.

## GO-PKG-006: Keep ordinary executable internals unexported

Identifiers in an ordinary `package main` do not need to be exported because the package is not imported as a library. Keep command wiring and implementation details unexported, and move reusable behavior into an importable package with its own coherent API.

Export from `package main` only for a verified external mechanism such as cgo exports, a supported plugin or shared-archive contract, generated integration, or another tool that consumes the symbol. Document that boundary instead of treating capitalization as harmless organization.

## GO-DOC-001: Document configuration and lifecycle

Document required setup, defaults, valid ranges, cancellation, cleanup, retry behavior, and side effects. State non-obvious context behavior, concurrency guarantees, caller-owned cleanup, and inspectable sentinel or typed errors. Do not restate conventions: ordinary context cancellation and obviously read-only or mutating concurrency behavior need documentation only when the API differs from normal expectations or the implementation makes the behavior surprising.

## GO-DOC-002: Keep documentation close to code

Keep exactly one package comment immediately above a package clause and update it with the implementation. Describe an ordinary library package's purpose and a `main` package's command behavior. Put substantial package documentation in `doc.go` when no natural primary file exists or a long comment would obscure implementation code; `doc.go` should otherwise contain only the package documentation and clause. Prefer examples that compile or are covered by tests when the behavior is subtle.

## GO-DOC-004: Inspect documentation as callers see it

Preview rendered documentation when adding or substantially changing exported APIs, package comments, headings, lists, or examples. Prefer an existing repository documentation check; otherwise use `go doc` or an available `pkgsite` workflow without adding a dependency solely for preview. Use blank comment lines for paragraphs, indentation for literal blocks, and runnable `Example` functions when compilation would protect the example from drift.
