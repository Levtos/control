# ha-platform control

`Levtos/control` is the public, versioned workflow and project-memory
repository for the active Home Assistant integrations.

## Platform decision

GitHub is the only active and historical source for code, Issues, Projects,
pull requests, Actions, releases, HACS distribution, evidence, and Project
Memory. GitLab, Plane, and Forgejo are retired and are not valid alternatives,
archives, or rollback targets.

The Home Assistant configuration repositories remain private. This
repository contains no live configuration, secrets, credentials, private
keys, Plane exports, or operational datasets.

## Working rules

- Start work from a GitHub Issue and read its description and comments.
- Add the Issue to the `Platform Workflow` Project and set its fields.
- Work on a branch and merge through a pull request.
- Stable releases are the default. Pre-releases require Benni's explicit
  decision.
- A merged PR is not live evidence. `Live` and `Live Verified` remain
  Benni's gate.
- End-to-end release work ends at a visible, installable HACS update.
- Keep repository-local tests separate from the central release workflow.
- Do not change Home Assistant, LXC 104, MCPHub, or LeanCTX from this repo.

## Documentation

- [Architecture](docs/architecture/platform.md)
- [Contracts](docs/contracts/overview.md)
- [Integration overview](docs/integrations/overview.md)
- [Operations](docs/operations/repositories.md)
- [Workflow](docs/workflow/README.md)
- [Release workflow](docs/workflow/hacs-release-workflow.md)
- [ADR index](docs/adr/README.md)
- [ADR 0002: GitHub-only governance](docs/adr/0002-github-only-governance.md)
- [UX standard](docs/ux/README.md)
- [Wiki / Project Memory snapshot](docs/wiki/README.md)
- [Issue migration mapping](docs/migration/issue-mapping.md)

The `docs/` tree is the only canonical Project Memory. A future Pages site,
if enabled, must be generated from this tree and must not become a second
editable source.
