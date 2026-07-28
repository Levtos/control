# ha-platform control

`Levtos/control` is the public, versioned workflow and project-memory
repository for the active Home Assistant integrations.

## Platform decision

GitHub is the primary platform for active code, Issues, Projects, pull
requests, Actions, releases, and HACS distribution. GitLab remains an
unchanged historical archive and rollback target at
https://gitlab.b-struck.de/ha-platform/control until a later, separately
verified archival decision.

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
- [Issue migration mapping](docs/migration/issue-mapping.md)

The `docs/` tree is the only canonical Project Memory. A future Pages site,
if enabled, must be generated from this tree and must not become a second
editable source.
