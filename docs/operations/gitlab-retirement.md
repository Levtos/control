# Retired platform record

This is a historical, non-authoritative migration record. Under
[ADR 0002](../adr/0002-github-only-governance.md), GitHub is the only active and
historical source for work, evidence, and Project Memory. GitLab, Plane, and
Forgejo are not valid alternatives, archives, or rollback targets.

## Already represented on GitHub

- The central control repository contains the current GitHub workflow, binding
  ADRs, and sanitized versioned Project Memory.
- The former Core Contracts target and gate records from GitLab Issues #57 and
  #66 are consolidated in the canonical Core Contracts GitHub Issue.
- Historical Issue mappings identify consolidated, split, and intentionally
  omitted material without pretending that every note or attachment was
  imported.
- The repositories that previously used another release path have their
  current GitHub Actions workflow documented in their own repository.

## Intentionally not copied into public GitHub

The following are not required for productive GitHub work and must not be
published merely to reach byte-for-byte parity:

- raw Plane exports, test-only pages, and private topology;
- GitLab/MCPHub operational notes and credentials;
- old GitLab issue templates, runner-specific instructions, and status reports;
- obsolete workspace instructions superseded by the current GitHub rules;
- private attachments, logs, and historical implementation chatter.

Their omission is recorded in the mapping and is not an indication that an
active product decision was silently discarded.

## Boundary of this repository

This file does not authorize or describe a platform recovery, service change,
LXC action, repository archive, repository deletion, or rename. Repository
lifecycle status is governed by
[operations/repositories.md](repositories.md); any irreversible infrastructure
decision requires a separate protected Issue and Benni's explicit approval.

Historical migration links remain only where needed to explain provenance. New
work, evidence, decisions, and recovery instructions belong in GitHub Issues and
the versioned `docs/` tree.
