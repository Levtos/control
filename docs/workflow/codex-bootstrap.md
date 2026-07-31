# Codex bootstrap

This is the canonical short Codex start bridge. Repository-local `AGENTS.md`
files link here; they do not copy the detailed governance in `control/docs/`.

1. Use CTX first when it is available in the local environment.
2. Read the complete GitHub Issue, all comments, labels, and Project fields.
3. Read ADR 0002, the relevant `control/docs/` pages, and the matching
   specification before implementation.
4. Treat GitHub as the only active and historical work, evidence, and memory
   source.
5. Work under exactly one Issue agent, recorded as `agent:codex` or
   `agent:claude`; technical completion is not Live.
6. For UX work, also follow ADR 0001, `Levtos/control#17`, and its derived
   documentation.
7. Keep local bridges short and repository-specific; do not duplicate detailed
   governance rules in feature repositories.

The Issue records the current scope, decisions, tests, PRs, risks, handoff, and
remaining Live gate. Benni owns the final Live verification.
