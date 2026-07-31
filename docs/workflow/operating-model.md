# Operating model

Benni is the product and live-system authority. ChatGPT prepares decisions
and Project Memory. Codex and Claude implement decided work. The active
technical GitHub actor must be recorded independently for commit, push, PR,
merge, workflow, and release; a cosmetic commit author is not sufficient.

GitHub Issues and comments are active workflow evidence. `control/docs/` is
the only durable Project Memory. GitHub is the only active and historical
source; GitLab, Plane, and Forgejo are retired and are not valid alternatives,
archives, or rollback targets. See [ADR 0002](../adr/0002-github-only-governance.md).

One Issue has one active implementation agent. Product uncertainty stops the
work and becomes a decision; unrelated findings become new Issues. Benni does
not need to micro-approve ordinary branch, commit, PR, merge, tag, or release
steps already covered by a decided Issue.

Evidence states:

- Missing: no technical evidence.
- Tests Pass: tests, review, or technical pilot passed.
- Live Verified: observed on the live HA system.

Workers may set Testing and Tests Pass with evidence. Benni owns Live and Live
Verified unless explicitly delegated.
