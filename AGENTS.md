# Codex operating rules

## Authority and scope

- Benni is the product and live-system decision maker.
- GitHub Issues and their comments record active decisions and work.
- `control/docs/` is the single durable Project Memory.
- GitHub is the only active and historical source for work, evidence, and
  Project Memory. GitLab, Plane, and Forgejo are retired and are not valid
  alternatives, archives, or rollback targets.
- Home Assistant configuration, LXC 104, MCPHub, and LeanCTX are outside
  this repository's scope.

## Issue-first flow

Before local technical work, use CTX as the first context step when it is
available in the local environment. If it is unavailable, record that fact and
continue without silently treating its absence as evidence. Installing or
reconfiguring CTX is not part of an unrelated Issue.

1. Classify the assignment as read-only evidence, architecture/decision
   clarification, or implementation of an already decided scope.
2. Read the complete Issue description and all comments.
3. Read relevant `control/docs/`, repository rules, Project fields, and any
   functional specification before technical work.
4. Add the Issue to the `Platform Workflow` Project and set Status, Type,
   Priority, Owner, Scope, Evidence, and Module only when known from evidence.
5. Use exactly one active implementation agent per Issue; record the agent as
   `agent:codex` or `agent:claude`.
6. Work from a clean clone or isolated worktree at a verified default-branch
   SHA. Never overwrite a dirty checkout.
7. Implement only the decided scope, test it, open a PR, inspect checks, and
   merge server-side when the Issue assignment authorizes that flow.
8. Record branch, commit, PR, merge SHA, tests, release, and risks on the
   Issue.

ChatGPT prepares triage, evidence, architecture clarification, Issue quality,
and review context, but does not make code, configuration, test, workflow,
deployment, or live-system changes. The Issue agent owns the decided
implementation scope; handoffs are explicit Issue notes, never parallel work.

New unrelated findings become separate Issues. Do not make a product decision
silently. Do not request a micro-approval for ordinary branch, commit, PR,
merge, tag, or release operations covered by the Issue decision.

## Decision and evidence discipline

Keep these layers separate in every Issue note and handoff:

- observation and timestamped episode;
- evidenced technical actual state;
- Benni's decided functional target state;
- implementation and changed files;
- tests and other technical verification;
- risks, blockers, and remaining decisions;
- Live and Live Verified evidence.

Technical evidence may expose contradictions, risks, or unknown dependencies,
but it does not choose the desired product state. If a product decision is
missing, stop the affected scope and record the question in the Issue.

Never silently turn uncertainty into a physical or product truth. Values such as
`unknown`, `unavailable`, `stale`, `suspect`, `restored`,
`source_conflict`, `provisional`, and `inferred` remain visible and
diagnosable. `fallback=reject` means that no replacement value is invented.
A safety consumer may conservatively block an action, but that does not change
the reported physical state.

Priorities, blockers, recovery, and resume behavior remain owned by their
domain. Do not introduce a global priority stack or simplify an existing
domain-specific path merely to make the workflow easier to describe. Preserve
decided existing behavior unless the Issue explicitly changes it.

## Identity and audit

The GitHub actor must be recorded separately for commit author, push actor,
PR actor, merge actor, workflow actor, and release actor. A different commit
author line is not sufficient identity evidence. Never print tokens or write
them to Issues, commits, logs, or files.

## Releases and HACS

- Stable `vX.Y.Z` releases are standard.
- Alpha, beta, RC, and other pre-releases require Benni's explicit decision.
- A tag must match the manifest version without the leading `v`.
- Direct GitHub releases are created by the tested GitHub Action, not by a
  manual release command.
- The technical E2E chain ends at a visible HACS update.
- Keep the Issue at Testing until live behavior is verified. Only Benni
  moves work to Live / Live Verified.

## Testing and safety

- Repository-local tests and central release automation are separate layers.
- Do not add runners, CI gates, or test infrastructure unless the Issue
  requires them.
- No force-push to protected branches. Never delete or replace existing
  tags or releases.
- Do not expose internal configuration, credentials, private keys, or
  unnecessary topology.
- Read the matching Lastenheft in the private configuration repository before
  any functional Home Assistant behavior change.
- Technical completion, Tests Pass, and a successful release do not establish
  Live or Live Verified. Those remain Bennis gate.

## Handoffs and documentation

A handoff must contain the current Ist/Soll separation, branch and commit,
changed files, tests, risks, open decisions or gates, and the next step. The
incoming agent reads and confirms the handoff before starting.

Stable, reusable process and architecture rules belong in `control/docs/`.
Concrete incidents, raw logs, hypotheses, rejected variants, and intermediate
states remain on the Issue. Feature-repository `AGENTS.md` files stay short
and point to the canonical bootstrap and `control/docs/`; they do not copy
domain implementation rules. LeanCTX mirrors this same process bridge in its
external configuration.

## Tools

Use `git`, `gh`, the official GitHub APIs, and `tools/github_workflow.py`.
Prefer structured arguments and JSON output. Avoid interactive OAuth or
credential-manager dialogs. The helper must fail clearly when Project scopes
are unavailable; do not work around that by printing or copying secrets.
