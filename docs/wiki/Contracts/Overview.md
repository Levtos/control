# Contracts — Übersicht

Contracts sind langlebige, von mehreren Integrationen konsumierte
Schnittstellen: Entity-Schemata, Attribute oder WebSocket-APIs. Änderungen
werden über ein Issue dokumentiert und möglichst additiv ausgerollt.

## Bekannte Producer und Consumer

| Contract | Producer | Consumer / Status |
|---|---|---|
| Geräte-Masters | core-devices | Feeder und Policies; watt-primäre Härtung je Geräteklasse bleibt ein eigenes Thema |
| Weather-Master | core-devices | climate-policy; Cutover historisch geplant |
| Kontext-Contracts | core-state | light, blind, door, media und notification policies |
| Media-Activity-Feed | media-state | core-state; Boundary statt Doppel-Detektion |
| Media-Kontext-Contracts | media-state | media-policy, light-policy, notification-router |
| Policy-Targets und Gates | media-policy | media-apply und media-core |
| WS benni_media.v1 | media-core | Media-Cockpit-Frontend |
| Title-Enums | title-classifier | media-state und light-policy |
| Look-Contract | light-policy | scene-presets |
| Wake-Contract | wake-planner | core-state |

## Core Contracts: Übergang statt stiller Umschaltung

Das GitLab-Wiki enthielt ältere Tabellen, in denen Opening- und Lock-Contracts
Core Devices zugeordnet waren. Das bleibt historische Ist-/Kompatibilitäts-
Provenienz und ist nicht automatisch der endgültige Ziel-Owner.

Core Contracts ist eine getrennte Foundation. Der aktuelle verifizierte Slice
ist read-only und Shadow-only. Die geplante nächste fachliche Phase kann
ausgewählte Home-Assistant-Entities veröffentlichen, aber nur nach:

- Definition der fachlichen Wahrheit und des Owners;
- Schema-, Attribute- und Degradierungsvertrag;
- Consumer-Inventar;
- Producer-vor-Consumer-Rollout;
- expliziter Allowlist statt vollständiger interner Exposition;
- Live-Evidence und dokumentiertem Rollback.

Aktiver Nachweis und offene Fragen stehen in
[benni-core-contracts#1](https://github.com/Levtos/benni-core-contracts/issues/1).

## Rollout-Regel

1. Producer oder Feeder zuerst testen und bereitstellen.
2. Bekannte Consumer prüfen und gezielt umstellen.
3. Alte Entity oder Berechnung erst entfernen, wenn alle Consumer repointet
   und verifiziert sind.
4. Pro Legacy-Entity genau einen neuen Owner dokumentieren.

Keine neue Master- oder Context-Entität wird nur als Alias oder zur
Entity-Reduktion angelegt. Private Normalizer bleiben privat; jede berechnete
Bedeutung hat genau einen Owner.

## Bekannte Fallen

- Entity-ID-Präfixe dürfen nicht aus einem idealisierten Slug abgeleitet
  werden; Bindings müssen auf verifizierte Quellen zeigen.
- Stale Quellzustände werden nicht ungeprüft als Gerätewahrheit verwendet.
- unavailable-, null- und degraded-Fälle müssen im Contract explizit sein.
- Combineds und Atomics aus der Legacy-Ära sind Kompatibilitäts- bzw.
  Retirement-Kandidaten und keine neue Zielarchitektur.

## UX-Grenze

Frontend-Komponenten konsumieren typisierte UX-Contracts. Sie greifen nicht
direkt auf rohe Home-Assistant-Entity-Strukturen zu und besitzen keine
Backend-Domänenlogik. Siehe [ADR 0001](../../adr/0001-ux-frontend-standard.md).
