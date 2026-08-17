# Google Go Style Skill

[![CI](https://github.com/faithk7/google-go-style-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/faithk7/google-go-style-skill/actions/workflows/ci.yml)

A Codex skill for writing, refactoring, and reviewing clear, idiomatic Go. It combines the current Google Go Style Guide with compatible Effective Go idioms and recurring composition patterns from handwritten Go standard-library packages.

## What it does

- Applies focused guidance for naming, packages, APIs, formatting, comments, errors, contexts, interfaces, concurrency, testing, and generated code.
- Shapes new code around compact package APIs, useful zero values, coherent method groups, direct control flow, and explicit ownership.
- Distinguishes normative rules from preferences and preserves deliberate repository-local conventions.
- Treats generated code, external interfaces, schemas, and compatibility contracts as explicit boundaries.
- Produces prioritized, rule-linked findings when reviewing code.

## Install

Clone the repository into your Codex skills directory:

```sh
git clone https://github.com/faithk7/google-go-style-skill.git \
  ~/.codex/skills/google-go-style-skill
```

Start a new Codex turn or session so the skill catalog refreshes. To update an existing installation:

```sh
git -C ~/.codex/skills/google-go-style-skill pull --ff-only
```

## Use

Invoke the skill explicitly with `$google-go-style`:

```text
Use $google-go-style to implement this Go package with a small public API and standard-library-like organization.
```

```text
Use $google-go-style to review this change, focusing only on interface ownership, error semantics, and tests.
```

```text
Use $google-go-style to refactor these types and methods without breaking exported API compatibility.
```

The skill can also activate implicitly for requests that explicitly ask for Google Go Style, Effective Go, idiomatic Go, or standard-library-like Go.

## Guidance model

The skill resolves overlapping guidance in this order:

1. Current Go semantics and standard-library documentation.
2. Deliberate repository-local instructions.
3. The pinned Google Go Style Guide.
4. Compatible supplementary guidance, including Effective Go.
5. Pinned `golang/go` source samples as non-normative composition exemplars.

Toolchain internals, generated tables, assembly, `unsafe`, bootstrap code, and compatibility machinery are not treated as general application patterns.

## Repository structure

```text
.
├── SKILL.md                  # Triggering, workflow, authority, and routing
├── agents/openai.yaml        # Codex-facing display metadata
├── references/               # Focused rules and source provenance
├── scripts/                  # Deterministic validation and source checks
└── tests/                    # Validator regression tests
```

Start with [SKILL.md](SKILL.md). Detailed rules are loaded progressively from [references](references), including [standard-library composition](references/standard-library-style.md) and [generated-code contracts](references/generated-code-and-contracts.md).

## Validate

The validation suite uses only Python's standard library:

```sh
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/validate.py
```

To also check whether the pinned Google Style Guide revision is current:

```sh
python3 scripts/validate.py --check-upstream
```

Validation covers skill metadata, local links, rule IDs, source declarations, reference registration, pinned source manifests, and the Effective Go crosswalk.

## Source policy

The exact upstream documents, revisions, sampled Go files, authority rules, and update policy are recorded in [references/source-map.md](references/source-map.md) and [references/source-manifest.json](references/source-manifest.json). Curated guidance is updated deliberately rather than regenerated wholesale from upstream text.
