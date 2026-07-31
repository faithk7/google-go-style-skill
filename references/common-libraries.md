# Common Library Decisions

Source: [`decisions.md#common-libraries`](https://github.com/google/styleguide/blob/gh-pages/go/decisions.md#common-libraries), with repository-local logging and security conventions taking precedence.

## GO-LIB-001: Keep flags at the program boundary

Define command-line flags in `package main` or its equivalent. Use snake_case for the external flag name and ordinary Go identifier style for the variable; configure reusable packages through Go APIs instead of package-level flags or hidden global state.

## GO-LIB-002: Match logging calls to their intent

Use the repository's logging package and structured fields. Prefer a non-formatting call when no formatting is needed, and know whether fatal or exit helpers run deferred cleanup before using them. Do not log secrets or duplicate an error at every layer.

## GO-LIB-003: Use cryptographic randomness for secrets

Use `crypto/rand` for keys, tokens, nonces, and other security-sensitive values. Use `math/rand` only for non-security behavior, and encode random bytes with a standard hexadecimal or base64 encoder when text is required.
