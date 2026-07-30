# Platform architecture

The active platform consists of independent Home Assistant integrations with
stable contracts. The public GitHub repositories contain integration code and
sanitized technical documentation. Private Home Assistant configuration
repositories remain separate.

## Signal flow

Raw Home Assistant entities → private normalizers/source adapters → device
and domain masters → context/fusion contracts → policies → apply layer.

Every calculated value has one owner. Masters provide stable domain truth;
policies decide targets; apply integrations execute actions. New public
contracts are Masters or clearly named Context/Fusion contracts. Existing
legacy Atomics and Combineds are compatibility/retirement candidates, not
new target architecture.

## UX boundary

The shared UX standard is defined in [ADR 0001](../adr/0001-ux-frontend-standard.md):
Svelte 5, Vite, TypeScript, typed REST/WebSocket contracts, a static bundle,
and a thin gateway. It must not duplicate domain logic or expose server-only
credentials. The active decision Issue is
[Levtos/control#17](https://github.com/Levtos/control/issues/17); the former
GitLab control#58 remains provenance.

## Core Contracts transition

Core Contracts is an independent Foundation integration, not a copy or silent
replacement of Core Devices. Its verified current slice is read-only and
Shadow-only: no public Home-Assistant entities, services, actuation or policy
logic. A future Published-Entity and Consumer-Cutover phase requires an
explicit allowlist, owner and consumer inventory, producer-first rollout,
live evidence and rollback. See
[benni-core-contracts#1](https://github.com/Levtos/benni-core-contracts/issues/1).

The older Core Devices L0 description remains useful historical compatibility
context, but it is not sufficient to decide the final ownership of Opening,
Lock or Activity Contracts.

## Operational boundary

GitHub is the active workflow and release platform. HACS consumes public
GitHub repositories. GitLab is retained read-only as historical archive and
rollback target until a separately verified archival decision. Home Assistant
instances, LXC 104, MCPHub, and private configuration remain outside this
repository.
