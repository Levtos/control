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

The shared UX standard is Svelte 5, Vite, TypeScript, typed REST/WebSocket
contracts, a static bundle, and a thin gateway. It must not duplicate domain
logic or expose server-only credentials. The binding ADR is tracked in the
history of the former GitLab control repository; future updates belong in a
versioned ADR under `docs/adr/`.

## Operational boundary

GitHub is the active workflow and release platform. HACS consumes public
GitHub repositories. GitLab is retained read-only as historical archive and
rollback target until a separately verified archival decision. Home Assistant
instances, LXC 104, MCPHub, and private configuration remain outside this
repository.
