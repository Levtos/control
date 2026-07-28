# Claude bootstrap

- GitHub is the active source of truth for code, Issues, Projects, PRs,
  Actions, releases, and HACS distribution.
- Read the complete Issue and all comments before work; add it to the
  `Platform Workflow` Project and set its known fields.
- Benni decides product behavior. Do not invent behavior or expand scope.
- Use a clean clone/worktree, a branch, a pull request, checks, and a
  server-side merge. Never overwrite dirty worktrees.
- Stable releases are standard. Pre-releases need Benni's explicit decision.
- The release chain ends at the visible HACS update. Testing is not Live;
  Live and Live Verified remain Benni's gate.
- `control/docs/` is the only durable Project Memory. GitLab is archive and
  rollback only; Plane and Forgejo are historical.
- Keep private HA configuration, credentials, tokens, LXC 104, MCPHub, and
  LeanCTX out of this repository.
- Use `git`, `gh`, and `tools/github_workflow.py`; never output secrets.
