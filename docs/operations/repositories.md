# Repository registry and lifecycle

`Levtos/control` and its `docs/` tree are the active, versioned workflow and
Project Memory source. The registry records lifecycle intent only; it never
performs an archive, deletion, migration, or rename.

## Lifecycle status values

| Status | Meaning | Required boundary |
|---|---|---|
| `active` | Current code, workflow, contract, or release source | Normal Issue-first work is allowed. |
| `legacy-in-operation` | Still used in operation or by consumers, but not the target architecture | No removal or silent rewiring; migrate only through a dedicated Issue. |
| `archive-candidate` | No active dependency is evidenced, but retention and recovery still need a decision | Candidate only; do not archive or stop anything from this registry. |
| `deletion-candidate` | Retention, dependency, recovery, and owner checks are complete enough for a separate deletion decision | Candidate only; deletion requires a new Issue and Benni's explicit approval. |

Status changes are documented in a GitHub Issue and reviewed through a PR when
the registry changes. An unproven assumption never upgrades a repository to an
archive- or deletion-candidate.

## Current registry

| Repository or group | Visibility | Lifecycle status | Boundary |
|---|---|---|---|
| `Levtos/control` | public | `active` | Sole active and historical workflow, evidence, and Project Memory source. |
| Public `Levtos` integrations other than the named legacy entry | public | `active` | Repository-local contracts and release workflows remain in each repository. |
| `Levtos/benni-core-devices` | public | `legacy-in-operation` | Remains in operation until the Core Contracts Published-Contract and Consumer-Cutover gate is live verified. |
| `Levtos/benni-core-contracts` | public | `active` | Successor Foundation integration; migration is separately Issue-governed. |
| Home Assistant configuration repositories | private | `active` | Outside this public registry's implementation scope and never copied here. |

The registry does not classify a retired hosting platform as an operational
repository. GitLab, Plane, and Forgejo are not valid active sources, archives,
or rollback targets; links in migration records are provenance only.

Each public integration repository must have a compact `AGENTS.md` and
`CLAUDE.md` bootstrap referring back to this control repository.

## Private repositories

Home Assistant configuration and instance repositories, including
`einhornzentrale` and the parents configuration, remain private. They are not
part of the public control repository or public Issue migration.

## Dirty checkouts

Local dirty states are operator-owned data. Cutover work must use fresh clones
or isolated worktrees from verified GitHub default-branch SHAs. Never reset,
clean, checkout over, or stage unrelated local changes.
