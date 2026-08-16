# Common Library Decisions

Sources: [`decisions.md#common-libraries`](https://github.com/google/styleguide/blob/gh-pages/go/decisions.md#common-libraries) and [`best-practices.md#complex-command-line-interfaces`](https://github.com/google/styleguide/blob/gh-pages/go/best-practices.md#complex-command-line-interfaces), with repository-local logging and security conventions taking precedence.

## GO-LIB-001: Keep flags at the program boundary

Define command-line flags in `package main` or its equivalent. Use snake_case for the external flag name and ordinary Go identifier style for the variable; configure reusable packages through Go APIs instead of package-level flags or hidden global state.

Keep a complex CLI as a thin client of reusable library code when the behavior also has non-CLI consumers. Subcommands do not each require a package; apply ordinary cohesion tests. Use a command framework only when its features justify the dependency, follow the repository's existing choice, and propagate the context supplied by the command rather than creating a new root context.

Create a root context at the process entry point when the framework requires one, then pass the framework-supplied context through handlers and reusable operations. Keep exit-code selection, final stderr rendering, and process termination at the outer CLI boundary; lower layers should return errors and let that boundary choose presentation and policy.

## GO-LIB-002: Match logging calls to their intent

Use the repository's logging package and structured fields. Prefer a non-formatting call when no formatting is needed, and know whether fatal or exit helpers run deferred cleanup before using them. Do not log secrets or duplicate an error at every layer.

## GO-LIB-003: Use cryptographic randomness for secrets

Use `crypto/rand` for keys, tokens, nonces, and other security-sensitive values. Use `math/rand` only for non-security behavior, and encode random bytes with a standard hexadecimal or base64 encoder when text is required.
