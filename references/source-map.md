# Source Map

This skill distills the public Google Go Style Guide into task-sized references. The upstream documents remain the authority when a bundled summary conflicts with its source; the authority section below governs conflicts among source families and repository-local rules.

## Upstream

- Landing page: <https://google.github.io/styleguide/go/>
- Repository: <https://github.com/google/styleguide/tree/gh-pages/go>
- Branch: `gh-pages`
- Tracked commit: see [`source-manifest.json`](source-manifest.json)

## Go tooling source

- [Go command `generate` documentation](https://pkg.go.dev/cmd/go#hdr-Generate_Go_files_by_processing_source): the tool-facing generated-file marker and execution semantics. It supplies the mechanical contract for recognizing generated Go source, not a general exemption from style or correctness review.

## Supplementary source

- [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments): official Go project review guidance for recurring idioms. The page describes itself as a supplement rather than a comprehensive style guide, so the current Google baseline remains controlling when they overlap.
- [Effective Go](https://go.dev/doc/effective_go): core language mechanics and established idioms. The page notes that it was written for Go's 2009 release and is not actively updated; it is used here as historical supplementary guidance rather than as the authority for modern language or ecosystem features.
- [Style guideline for Go packages](https://rakyll.org/style-packages/) ([archived snapshot](https://web.archive.org/web/20260110162648/https://rakyll.org/style-packages/)): 2017 package-organization advice used only where it remains compatible with modules and the current Google baseline. Its GOPATH layout, blanket singular-name, vanity-import-comment, and import-alias prescriptions are not adopted as universal rules.

## Reference implementation

- [`golang/go` at `72aa6db7943024b48c4d41c1fbc32b57b9fa036e`](https://github.com/golang/go/tree/72aa6db7943024b48c4d41c1fbc32b57b9fa036e): recurring composition patterns sampled across handwritten `bytes`, `io`, `archive/zip`, `net/http`, `os`, `sync`, and `slices` code. The samples inform package vocabulary, zero-value design, responsibility-based files, method grouping, direct control flow, and contract comments. Toolchain internals, generated tables, assembly, `unsafe`, bootstrap, and compatibility mechanisms are excluded unless a target has the same constraints.

## Non-authoritative case study

- [`openai/openai-cli` at `68e3e707ef68bebda13e638fafdb4a882ccafedc`](https://github.com/openai/openai-cli/tree/68e3e707ef68bebda13e638fafdb4a882ccafedc): reviewed for generated-command boundaries, external interface names, CLI error presentation, injected I/O, and platform checks. It is practical evidence only; its generated layout, testing dependencies, and local inconsistencies do not override the authority order below.

## Authority

Use the current Go specification and standard-library documentation for language behavior. Apply deliberate repository-local style next, then the pinned Google Go Style Guide, and use supplementary sources only for compatible context. Within the Google baseline, `guide.md` supplies principles, `decisions.md` states the normative style position, and `best-practices.md` supplies contextual techniques and tradeoffs. Historical examples do not override modern rules for generics, modules, package paths, error wrapping, initialization, panic/recover, contexts, or library APIs. Use the pinned `golang/go` source only as a non-normative composition exemplar after those decisions are resolved; observed code never overrides the hierarchy.

## Document map

| Skill reference | Upstream document | Relevant sections |
| --- | --- | --- |
| `principles.md` | `guide.md`, `decisions.md` | Style principles; core guidelines; explicit non-decisions |
| `formatting-and-imports.md` | `guide.md`, `decisions.md`, `best-practices.md` | Formatting; imports; literal formatting |
| `naming-and-comments.md` | `decisions.md`, `best-practices.md` | Naming; variable scope; repetition; commentary; documentation |
| `errors-context-and-logging.md` | `decisions.md`, `best-practices.md` | Errors; contexts; logging |
| `interfaces-and-concurrency.md` | `decisions.md`, `best-practices.md` | Interfaces; goroutine lifetimes; channels; global state |
| `language-and-api-design.md` | `decisions.md`, `best-practices.md` | Language; function arguments; variables; APIs |
| `standard-library-style.md` | Pinned `golang/go` handwritten package samples; Go Code Review Comments | Package vocabulary; zero values and ownership; file and method organization; direct implementation; contract comments; toolchain exclusions |
| `generated-code-and-contracts.md` | Go command `generate` documentation; `best-practices.md` | Generated markers; authoritative edit points; external interface and schema contracts; regeneration |
| `packages-and-documentation.md` | `best-practices.md`; Rakyll package article | Package size; utility packages; file organization; import paths; executable exports; documentation |
| `testing.md` | `decisions.md`, `best-practices.md` | Test structure; test failures; helpers |
| `common-libraries.md` | `decisions.md` | Flags; logging; contexts; cryptographic randomness |
| `effective-go.md` | [Effective Go](https://go.dev/doc/effective_go) | Formatting; commentary; names; semicolons; control structures; functions; data; initialization; methods; interfaces; blank identifier; embedding; concurrency; errors; web-server example |

Use upstream section anchors where available when a decision needs more detail than the summary provides. Do not treat this index as a license to load every reference for every task.

## Focused provenance

| Guidance lens | Upstream sections | Curated rules |
| --- | --- | --- |
| Naming | [`decisions.md#naming`](https://github.com/google/styleguide/blob/gh-pages/go/decisions.md#naming), [`decisions.md#repetition`](https://github.com/google/styleguide/blob/gh-pages/go/decisions.md#repetition), [`best-practices.md#naming`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#naming), [`best-practices.md#shadowing`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#shadowing) | `GO-NAME-*`, `GO-COMMENT-*` |
| Package and API boundaries | [`decisions.md#package-names`](https://github.com/google/styleguide/blob/gh-pages/go/decisions.md#package-names), [`decisions.md#interfaces`](https://github.com/google/styleguide/blob/gh-pages/go/decisions.md#interfaces), [`best-practices.md#package-size`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#package-size), [`best-practices.md#global-state`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#global-state), [`best-practices.md#interfaces`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#interfaces) | `GO-PKG-*`, `GO-API-*`, `GO-STATE-*`, `GO-LIB-001` |
| Clarity | [`guide.md#clarity`](https://github.com/google/styleguide/blob/gh-pages/go/guide.md#clarity), [`decisions.md#commentary`](https://github.com/google/styleguide/blob/gh-pages/go/decisions.md#commentary), [`decisions.md#language`](https://github.com/google/styleguide/blob/gh-pages/go/decisions.md#language), [`best-practices.md#documentation`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#documentation) | `GO-PRINCIPLE-*`, `GO-FMT-*`, `GO-DOC-*`, `GO-LANG-*` |
| Effectiveness | [`guide.md#least-mechanism`](https://github.com/google/styleguide/blob/gh-pages/go/guide.md#least-mechanism), [`best-practices.md#function-argument-lists`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#function-argument-lists), [`best-practices.md#tests`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#tests), [`best-practices.md#string-concatenation`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#string-concatenation) | `GO-LANG-005`, `GO-LANG-013`, `GO-TEST-*` |
| Context and exceptions | [`decisions.md#non-decisions`](https://github.com/google/styleguide/blob/gh-pages/go/decisions.md#non-decisions), [`best-practices.md#error-handling`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#error-handling), [`best-practices.md#variable-declarations`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#variable-declarations) | `GO-PRINCIPLE-006`, `GO-ERR-*`, `GO-LANG-012` |
| Generated code and contracts | [Go command `generate` documentation](https://pkg.go.dev/cmd/go#hdr-Generate_Go_files_by_processing_source), [`best-practices.md#interfaces`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#interfaces) | `GO-GEN-*`, compatible `GO-NAME-*`, `GO-API-*`, and `GO-TEST-*` rules |
| Standard-library composition | Pinned [`golang/go` samples](https://github.com/golang/go/tree/72aa6db7943024b48c4d41c1fbc32b57b9fa036e/src), [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments) | `GO-STD-*` as compatible implementation heuristics; related `GO-PKG-*`, `GO-NAME-*`, `GO-LANG-*`, and `GO-API-*` rules remain controlling |

## Update policy

Run `python3 scripts/validate.py` after changing the skill. Run `python3 scripts/validate.py --check-upstream` periodically to include source-manifest freshness. When upstream changes, review the affected sections, update only the relevant curated references, and rerun validation. Do not silently replace curated guidance with generated upstream text.
