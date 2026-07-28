# Verification and efficiency

Use the smallest evidence that establishes the requested claim:

- `git diff --check` and focused repository tests for code changes.
- PR checks and current merge SHA for server-side integration.
- tag, manifest, release type, and Action run for a release.
- HACS read-only state for visible availability.
- live HA behavior only for the explicit human Live gate.

Do not infer a release, merge, deployment, or live result from a local commit
or a successful push. Record exact URLs, IDs, timestamps, actors, and
request/run IDs without secret values.
