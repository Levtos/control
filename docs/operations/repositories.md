# Operational repositories

## Public active repositories

The active HACS/integration repositories are public under `Levtos` and use
GitHub as the primary code and release location. Each repository must have a
compact `AGENTS.md` and `CLAUDE.md` bootstrap referring back to this control
repository.

## Private repositories

Home Assistant configuration and instance repositories, including
`einhornzentrale` and the parents configuration, remain private. They are not
part of the public control repository or public Issue migration.

## Archive and rollback

The former GitLab projects remain intact as historical archive and rollback
targets. No GitLab project, tag, release, issue, wiki page, user, token, or
runner is deleted by the GitHub cutover.

## Dirty checkouts

Local dirty states are operator-owned data. Cutover work must use fresh clones
or isolated worktrees from verified GitHub default-branch SHAs. Never reset,
clean, checkout over, or stage unrelated local changes.
