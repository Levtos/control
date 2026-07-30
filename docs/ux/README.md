# Gemeinsamer UX-Standard

Die verbindliche Technologie- und Designentscheidung steht in
[ADR 0001](../adr/0001-ux-frontend-standard.md). Das zugehörige GitHub-Issue
ist [Levtos/control#17](https://github.com/Levtos/control/issues/17); die
historische Fachentscheidung ist
[GitLab control#58](https://gitlab.b-struck.de/ha-platform/control/-/work_items/58).

## Kurzfassung

- 19 native Home-Assistant-Backends bleiben unabhängig.
- Gemeinsame UX: statisches Svelte-5-/Vite-Bundle plus schlankes Gateway.
- Fachlogik und Datenhoheit bleiben in den Integrationen.
- Snapshots laufen über REST, Live-Änderungen über typisierte WebSockets.
- Authentifizierung und Tokens bleiben serverseitig.
- Designsystem: Graphite Dark mit semantischen Akzentfarben.
- Verbindliche UI-Zustände: loading, ready, empty, stale, degraded,
  unavailable, reconnecting, offline, error und blocked.

## Für neue UX-Arbeiten

Vor Beginn sind ADR 0001, der betroffene Contract und das zuständige
GitHub-Issue zu lesen. Eine neue Seite darf keine rohe Home-Assistant-
Entity-Struktur, eigene Backend-Domänenlogik oder Frontend-Secrets als
implizite Schnittstelle einführen.

Ein abweichender Stack, ein anderes Authentifizierungsmodell, eine andere
Deployment-Grundform oder eine geänderte Statussemantik braucht zuerst eine
neue fachliche Entscheidung und eine ersetzende ADR.

## Core Contracts

Die Core-Contracts-UX ist ein read-only Shadow-only-Anwendungsfall dieses
Standards. Sie zeigt versionierte Contract-, Graph- und Diagnose-Payloads,
erzeugt aber im aktuellen Slice keine öffentlichen Entities, Services oder
Actuation. Details und Gates stehen im
[Wiki-Snapshot](../wiki/Integrations/Core-Contracts/UX.md) und in der
[Core-Contracts-Provenienz](https://github.com/Levtos/benni-core-contracts/issues/1).

## Datenschutz

Dieses Repository enthält nur öffentliche, bereinigte Architektur- und
Projektinformationen. Live-URLs, lokale IP-Adressen, Zugangsdaten,
Home-Assistant-Konfiguration und private Betriebsdaten gehören nicht hierher.
