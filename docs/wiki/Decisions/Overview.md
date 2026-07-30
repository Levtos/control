# Entscheidungen — ADR-Prinzip

## Zweck

Dauerhafte Architektur- und Produktentscheidungen müssen ohne Chat-Historie
auffindbar bleiben. Benni ist der fachliche Entscheider; ein mit Benni
entschiedenes Arbeits-Issue ist die fachliche Freigabe.

## Ablauf

1. Entscheidungsbedarf als GitHub-Issue vom Typ decision dokumentieren.
2. Entscheidung, Begründung und Akzeptanz im Issue festhalten.
3. Dauerhafte Architekturentscheidung als ADR unter docs/adr versionieren.
4. Betroffene Projekt-Memory-Seiten im Abschluss-Gate nachziehen.

## Verabschiedete Entscheidung

| ADR | Titel | Status | Aktives GitHub-Issue | Historische Quelle |
|---|---|---|---|---|
| [ADR 0001](../../adr/0001-ux-frontend-standard.md) | Einheitlicher UX-, Technologie- und Designstandard | angenommen und bindend | [control#17](https://github.com/Levtos/control/issues/17) | [GitLab control#58](https://gitlab.b-struck.de/ha-platform/control/-/work_items/58) |

ADR 0001 legt die 19 nativen Backends, das statische Svelte-5-/Vite-Bundle,
das dünne Gateway, Graphite Dark, typisierte REST-/WebSocket-Contracts und
die verbindlichen UI-Zustände fest.

## Core Contracts

Die Foundation-Entscheidung aus GitLab control#57 wird nicht durch die
UX-ADR ersetzt. Der aktuelle GitHub-Nachweis steht in
[benni-core-contracts#1](https://github.com/Levtos/benni-core-contracts/issues/1).
Der verifizierte Stable-Stand ist v0.1.1; historische Alpha-Angaben werden
nicht als aktuelle Live-Fakten ausgegeben.

## Regel

Es werden keine Entscheidungen aus alten Tickets oder Wikis rückwirkend
erfunden. Historische Quellen bleiben auffindbar, aber ein aktueller
Zielzustand braucht ein aktives Issue und eine überprüfbare Akzeptanz.
