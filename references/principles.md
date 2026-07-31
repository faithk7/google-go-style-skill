# Principles

Source: [`guide.md`](https://github.com/google/styleguide/blob/gh-pages/go/guide.md), “Style principles” and “Core guidelines”.

## GO-PRINCIPLE-001: Optimize for clarity

Make the code's behavior and intent easy to identify. Prefer explicit names, direct control flow, and local reasoning over compressed expressions or clever indirection.

Ask two questions during review:

1. What is the code actually doing?
2. Why is it doing that?

Comments should answer the second question when the reason is not obvious from the code.

## GO-PRINCIPLE-002: Prefer simplicity and least mechanism

Use the fewest language features, abstractions, and moving parts needed for the requirement. Do not add a framework, interface, generic helper, or configuration layer until a concrete problem justifies it.

## GO-PRINCIPLE-003: Keep code concise without hiding behavior

Remove repetition and incidental complexity, but do not shorten code by hiding important state transitions, error paths, or ownership. A few extra lines are preferable when they make a critical decision visible.

## GO-PRINCIPLE-004: Design for maintainability

Make changes easy to review, test, extend, and safely remove. Keep related behavior together, choose stable boundaries, document invariants, and avoid coupling callers to implementation details.

## GO-PRINCIPLE-005: Follow local consistency

Use existing package conventions when they are coherent and do not violate correctness. Introduce a new pattern only when it solves a real problem, and keep the migration scope explicit.

## GO-PRINCIPLE-006: Preserve explicit non-decisions

Do not turn unresolved style debates into universal requirements. In particular, permit locally consistent choices between zero-value declarations and equivalent short declarations, empty composite literals and equivalent `new`/`make` forms, `cmp.Diff` argument order, and `errors.New` versus `fmt.Errorf` for a non-formatted string. Require clarity and a documented contract where the choice affects behavior.
