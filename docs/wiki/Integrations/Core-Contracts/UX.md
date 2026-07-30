# Core Contracts UX

## Status und Herkunft

- Backend: benni_core_contracts
- Fachliche Quelle: [GitLab control#57](https://gitlab.b-struck.de/ha-platform/control/-/work_items/57)
- UX-Quelle: [GitLab control#59](https://gitlab.b-struck.de/ha-platform/control/-/work_items/59)
- UX-Standard: [GitHub control#17](https://github.com/Levtos/control/issues/17)
- Historische Binding-Entscheidung: [GitLab control#58](https://gitlab.b-struck.de/ha-platform/control/-/work_items/58)
- Aktive Repository-Provenienz: [benni-core-contracts#1](https://github.com/Levtos/benni-core-contracts/issues/1)
- Technischer Wiki-Snapshot: 0.2.0-alpha.1
- Verifizierter GitHub-Stable-Hinweis: v0.1.1
- Fachliche und visuelle Live-Abnahme: offen, solange das Issue testing bleibt

Die unterschiedlichen Versionsangaben sind absichtlich getrennt: Die
historische Wiki-Seite beschreibt einen geplanten Alpha-Slice, während die
aktuelle GitHub-Dokumentation den verifizierten Stable-Stand führt. Vor einer
Live- oder Published-Entity-Aussage muss dieser Unterschied im Issue geklärt
werden.

## Zweck und Grenzen

Core Contracts ist eine unabhängige, read-only Shadow-only-Foundation. Die UX
macht interne, versionierte Contract- und Diagnose-Daten prüfbar. Im aktuellen
Slice werden keine öffentlichen Home-Assistant-Entities erzeugt, keine
Services registriert, keine Actuation ausgeführt und keine Policy-
Entscheidungen getroffen.

Nicht enthalten sind eine vollständige Umbrella-UX, ein fleetweiter
Frontend-Umbau, ConfigEntry-Schreibpfade oder ein Consumer-Cutover. Ein
späterer Published-Entity-Slice ist nur mit expliziter Allowlist,
Owner-Dokumentation, Consumer-Prüfung und Live-Gate zulässig.

## Transport und Panel

Das statische Svelte-5-/Vite-Bundle trennt App-Shell, Design-Tokens,
UI-Primitiven, Transport, typisierte Stores und fachliche Ansichten.

Das read-only Panel verwendet ausschließlich diese fachlichen Befehle:

    benni_core_contracts/list_contracts
    benni_core_contracts/get_contract
    benni_core_contracts/get_diagnostics
    benni_core_contracts/get_graph
    benni_core_contracts/get_health

Angezeigt werden reale Payloads, Revisionen, stabile IDs, Feldwerte, Health,
Freshness, Safety, Fallback, Root Cause, Quell-Entities,
Degradierungsdauer und Consumer-Effekt. Fehler-, Stale- und Blocked-Zustände
bleiben sichtbar.

Fixture-Preview ist ausschließlich eine lokale Entwicklungshilfe und muss als
nicht live markiert werden. Home Assistant verwendet keine Preview-Daten und
speichert keine Tokens oder Secrets im Frontend.

## Technische Nachweise aus der historischen Quelle

Die historische Wiki-Seite dokumentierte erfolgreiche lokale Nachweise für
Svelte-Check, Vitest, Python-Tests, compileall, Repository-Validation und den
Vite-Produktionsbuild sowie die Boundary-Aussage: null Entities, null
Services, null Actuation und null Policy-Imports.

Diese Angaben sind technische Provenienz, keine aktuelle Live-Evidence. Ein
Release, ein lokaler Test oder ein GitHub-Merge ersetzt keine autorisierte
Home-Assistant-Live-Verifikation.

## Rollout-Grenze

Der UX-Release kann technisch veröffentlicht werden, während das Backend-
Live-Evidence-Gate offen bleibt. Die UX darf einen offenen oder degradierten
Backend-Zustand anzeigen, aber nicht durch historische Fixtures verdecken.

Weitere fachliche Gates und die geplante Published-Entity-/Consumer-Phase
stehen im Issue [benni-core-contracts#1](https://github.com/Levtos/benni-core-contracts/issues/1).
