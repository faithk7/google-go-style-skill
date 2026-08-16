# Generated Code and External Contracts

Sources: the Go command's [`generate` documentation](https://pkg.go.dev/cmd/go#hdr-Generate_Go_files_by_processing_source), [`best-practices.md#interfaces`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#interfaces), and the Google guide's principles of clarity, simplicity, and local consistency.

## GO-GEN-001: Establish provenance and the authoritative edit point

Determine whether a file is handwritten, generated, schema-derived, or constrained by an external interface before reviewing its style. Search for generator commands, templates, schemas, IDLs, build scripts, and repository instructions; do not infer the edit point from a filename or directory alone.

Go tooling recognizes generated source only when a line matching `^// Code generated .* DO NOT EDIT\.$` appears before the first non-comment, non-blank text. A repository-specific header may still inform maintainers, but it does not satisfy that tool-facing convention. Treat a missing or noncanonical marker as a generator or repository-process issue, not as permission to edit repeatable output by hand.

## GO-GEN-002: Preserve external contracts without spreading their style

Keep names and shapes required by an implemented external interface, wire protocol, schema, serialization format, or compatibility promise even when they differ from preferred handwritten Go style. Verify the constraint at its source instead of assuming that every generated-looking name is immutable.

Constrain exceptions to the contract boundary. Handwritten adapters, local variables, helper methods, and APIs that are not prescribed by the contract should remain idiomatic. Do not copy schema-derived repetition, underscores, `Get` prefixes, package state, or generated file organization into unconstrained code merely for visual consistency.

## GO-GEN-003: Fix systematic output at the source and verify regeneration

Change the generator, template, schema, or IDL when a problem repeats across generated output. Regenerate with the repository's documented command, inspect the complete diff for unexpected files or API changes, and run formatting plus the affected build and tests. Include relevant target platforms when generation changes OS-specific files or build constraints.

If the authoritative source or generator is unavailable or outside the task, report the generated file as evidence and state the limitation. Do not hide a correctness, security, data-integrity, or compatibility problem because its immediate evidence is generated; direct the durable fix to the owning source.
