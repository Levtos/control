# GitLab retirement checklist

Status: GitHub is the active workflow. GitLab remains a temporary historical
archive and rollback source until the deletion gate below is completed.

## Already represented on GitHub

- The central control repository contains the current GitHub-first workflow,
  the binding UX ADR, and a sanitized versioned Wiki snapshot.
- The former Core Contracts target and gate records from GitLab Issues #57 and
  #66 are consolidated in the canonical Core Contracts GitHub Issue.
- Historical Issue mappings identify consolidated, split, and intentionally
  omitted material without pretending that every note or attachment was
  imported.
- The old GitLab release include has an active GitHub Actions replacement in
  the repositories that used it.

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

## Deletion gate

Before deleting the GitLab LXC, verify all of the following:

1. The five repositories that referenced the central GitLab release include no
   remaining active GitLab CI dependency.
2. Each affected repository has a working GitHub Action for its release path;
   repositories with GitLab-only tests retain equivalent GitHub test coverage.
3. Current GitHub default branches, tags, releases, Issues, ADRs, and Wiki
   snapshot are readable and their resulting commit SHAs are recorded.
4. A protected, recoverable export or snapshot of the private GitLab instance
   exists, including repositories, Issues/notes, attachments, CI variables,
   runners, registries, artifacts, webhooks, and relevant configuration.
5. No runtime system, Home Assistant integration, MCPHub component, router,
   reverse proxy, or public endpoint still depends on the GitLab LXC.
6. The GitLab service is stopped and monitored through a retention window.
7. Benni gives a separate final confirmation for irreversible LXC deletion.

The deletion gate is deliberately separate from the documentation and
repository cutover. It prevents a missing historical artifact from becoming a
runtime outage while allowing normal development to continue on GitHub.

## Recovery boundary

If a missing historical item is discovered before deletion, recover it from the
protected export or temporary GitLab snapshot and add only the sanitized,
current decision to the appropriate GitHub Issue or documentation page. Do not
restore GitLab as an active workflow source.
