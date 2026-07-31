# Claude bootstrap

- GitHub is the active source of truth for code, Issues, Projects, PRs,
  Actions, releases, and HACS distribution.
- GitHub is also the only historical source for work, evidence, and Project
  Memory; GitLab, Plane, and Forgejo are not valid alternatives, archives, or
  rollback targets.
- Read the complete Issue and all comments before work; add it to the
  `Platform Workflow` Project and set its known fields.
- Benni decides product behavior. Do not invent behavior or expand scope.
- ChatGPT remains read/review/assignment-only; exactly one Issue agent,
  identified by `agent:codex` or `agent:claude`, performs implementation work.
- Use a clean clone/worktree, a branch, a pull request, checks, and a
  server-side merge. Never overwrite dirty worktrees.
- Stable releases are standard. Pre-releases need Benni's explicit decision.
- The release chain ends at the visible HACS update. Testing is not Live;
  Live and Live Verified remain Benni's gate.
- `control/docs/` is the only durable Project Memory; see ADR 0002 and the
  workflow documentation for ownership, handoff, lifecycle, and live gates.
- Keep private HA configuration, credentials, tokens, LXC 104, MCPHub, and
  LeanCTX out of this repository.
- Use `git`, `gh`, and `tools/github_workflow.py`; never output secrets.
