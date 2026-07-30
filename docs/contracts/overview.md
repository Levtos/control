# Contracts overview

Contracts are long-lived interfaces consumed by more than one integration.
They must be typed, versioned, documented, and changed additively where
possible. Producer and feeder changes are deployed before consumers.

## Ownership

- Core Devices owns normalized device and primitive domain truth.
- Core State and Media State own context/fusion meaning.
- Policies own decisions such as target audio, blind position, heating
  profile, and plug-cut safety.
- Apply integrations execute decisions and do not rebuild domain truth.
- UX clients consume typed snapshots/events and do not own backend logic.

## Core Contracts transition

Core Contracts is a separate Foundation integration. The verified current
release is v0.1.1 and its current slice is read-only and Shadow-only: no
public entities, services, actuation or policy imports. The future Published-
Entity phase is an explicit allowlist and consumer-cutover decision, not an
automatic migration of every old Core Devices ticket.

The former Wiki atlas associated Opening and Lock Contracts with Core Devices.
That is historical compatibility context. Activity State, the three-state
Opening contract, Lock/Unlock semantics and the new U200 evidence must be
reconciled against the current Core Contracts implementation before any
consumer or public entity is switched. The active technical record is
[benni-core-contracts#1](https://github.com/Levtos/benni-core-contracts/issues/1).

## Change requirements

Before changing a contract, document the owner, consumers, owned attributes,
projected attributes, compatibility behavior, and rollback. Do not silently
create duplicate calculations, circular dependencies, or public entities for
private helper calculations.

The currently verified public Core Contracts release is `v0.1.1`; older alpha
labels are historical and must not be used as the current stable description.
