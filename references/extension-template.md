# Extension Template

Use this template for a repository-local `.go-style.md` or a team policy layered on top of the Google baseline. Keep additions narrow and explain why the local rule is needed.

```markdown
# Local Go Style

## Rule: LOCAL-XXX

- Priority: Must | Should | May
- Applies to: package, layer, or file pattern
- Rule: one actionable sentence
- Rationale: behavior, tooling, compatibility, or operational reason
- Example: a small good/bad example when ambiguity is likely
- Exception: when the rule does not apply
- Verification: command, test, or review evidence
- Upstream relationship: follows, narrows, or intentionally differs from GO-XXXX-XXX
```

Local rules must not silently weaken correctness, error handling, cancellation, security, or API contracts. If a local rule conflicts with the Google baseline, name the conflict and keep the exception scoped.
