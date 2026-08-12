# Codex bootstrap

This is the canonical short Codex start bridge. Repository-local `AGENTS.md`
files link here; they do not copy the detailed governance in `control/docs/`.

1. Use CTX first when it is available in the local environment. If it is not
   available, record that fact and continue without treating the absence as
   technical evidence.
2. Classify the assignment: read-only evidence, decision clarification, or
   implementation of an already decided scope.
3. Read the complete GitHub Issue, all comments, labels, and Project fields.
4. Read ADR 0002, the relevant `control/docs/` pages, repository rules, and
   the matching specification before technical work.
5. Treat GitHub as the only active and historical work, evidence, and memory
   source.
6. Keep observation, evidenced Ist, decided Soll, implementation, tests,
   risks, open gates, and Live evidence separate.
7. Never invent a product decision or silently replace uncertainty. Preserve
   `unknown`, `unavailable`, `stale`, `source_conflict`, and
   `fallback=reject` as visible diagnostic outcomes.
8. Keep domain priorities, blockers, recovery, and existing paths
   domain-specific; do not create a global replacement stack.
9. Work under exactly one Issue agent, recorded as `agent:codex` or
   `agent:claude`. Codex is the current default for new or explicitly
   reassigned work; Claude is an explicit per-Issue exception.
10. Technical completion and Tests Pass are not Live. Benni owns Live and
    Live Verified.
11. Keep local bridges short and repository-specific; do not duplicate
    detailed governance or feature logic in integration repositories.

The Issue records the current scope, decisions, tests, PRs, risks, handoff, and
remaining Live gate. Benni owns the final Live verification.
