# Codex operating rules

## Authority and scope

- Benni is the product and live-system decision maker.
- GitHub Issues and their comments record active decisions and work.
- `control/docs/` is the single durable Project Memory.
- GitLab is historical archive and rollback target only.
- Plane and Forgejo are historical/out of service and must not be used.
- Home Assistant configuration, LXC 104, MCPHub, and LeanCTX are outside
  this repository's scope.

## Issue-first flow

1. Read the complete Issue description and all comments.
2. Read relevant `control/docs/`, repository rules, and any functional
   specification before code work.
3. Add the Issue to the `Platform Workflow` Project and set Status, Type,
   Priority, Owner, Scope, Evidence, and Module when known.
4. Use one active implementation agent per Issue.
5. Work from a clean clone or isolated worktree at a verified default-branch
   SHA. Never overwrite a dirty checkout.
6. Implement only the decided scope, test it, open a PR, inspect checks, and
   merge server-side.
7. Record branch, commit, PR, merge SHA, tests, release, and risks on the
   Issue.

New unrelated findings become separate Issues. Do not make a product
decision silently. Do not request a micro-approval for ordinary branch,
commit, PR, merge, tag, or release operations covered by the Issue decision.

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

## Tools

Use `git`, `gh`, the official GitHub APIs, and `tools/github_workflow.py`.
Prefer structured arguments and JSON output. Avoid interactive OAuth or
credential-manager dialogs. The helper must fail clearly when Project scopes
are unavailable; do not work around that by printing or copying secrets.
