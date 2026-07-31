# Source Map

This skill distills the public Google Go Style Guide into task-sized references. The upstream documents remain the authority when a local rule and a summary conflict.

## Upstream

- Landing page: <https://google.github.io/styleguide/go/>
- Repository: <https://github.com/google/styleguide/tree/gh-pages/go>
- Branch: `gh-pages`
- Tracked commit: see [`source-manifest.json`](source-manifest.json)

## Supplementary source

- [Effective Go](https://go.dev/doc/effective_go): core language mechanics and established idioms. The page notes that it was written for Go's 2009 release and is not actively updated; it is used here as historical supplementary guidance rather than as the authority for modern language or ecosystem features.

## Document map

| Skill reference | Upstream document | Relevant sections |
| --- | --- | --- |
| `principles.md` | `guide.md`, `decisions.md` | Style principles; core guidelines; explicit non-decisions |
| `formatting-and-imports.md` | `guide.md`, `decisions.md`, `best-practices.md` | Formatting; imports; literal formatting |
| `naming-and-comments.md` | `decisions.md`, `best-practices.md` | Naming; variable scope; repetition; commentary; documentation |
| `errors-context-and-logging.md` | `decisions.md`, `best-practices.md` | Errors; contexts; logging |
| `interfaces-and-concurrency.md` | `decisions.md`, `best-practices.md` | Interfaces; goroutine lifetimes; channels; global state |
| `language-and-api-design.md` | `decisions.md`, `best-practices.md` | Language; function arguments; variables; APIs |
| `packages-and-documentation.md` | `best-practices.md` | Package size; utility packages; documentation |
| `testing.md` | `decisions.md`, `best-practices.md` | Test structure; test failures; helpers |
| `common-libraries.md` | `decisions.md` | Flags; logging; contexts; cryptographic randomness |
| `effective-go.md` | [Effective Go](https://go.dev/doc/effective_go) | Declarations; control structures; defer; allocation; slices; maps; initialization; receivers; interfaces; embedding; concurrency; errors; panic/recover |

Use upstream section anchors where available when a decision needs more detail than the summary provides. Do not treat this index as a license to load every reference for every task.

## Update policy

Run `python3 scripts/update-source-manifest.py --check` periodically. When upstream changes, review the affected sections, update only the relevant curated references, and then run the skill validation and example checks. Do not silently replace curated guidance with generated upstream text.
