# Plattform-Architektur — bereinigte Wiki-Fassung

Diese Seite überführt den früheren Wiki-Atlas. Teile des Atlas wurden vor der
Core-Contracts-Entscheidung geschrieben und sind deshalb als historische
Zwischenbeschreibung zu lesen.

## Schichtenmodell der historischen Integration

| Schicht | Rolle | Historische Zuordnung |
|---|---|---|
| L0 Foundation | Roh-Entitäten zu Masters und stabilen Domain-Contracts normalisieren | core-devices |
| L1 Context / Feeder | Bedeutung ableiten, nichts entscheiden | core-state, media-state, title-classifier |
| L2 Policy | entscheiden, was passieren soll und warum | light, blind, media, climate, plug, door, notification |
| L3 Render / Apply | Policy-Entscheidungen ausführen | scene-presets, media-apply |
| L4 UX | Panels, Umbrella und Gateways ohne Business-Logik | media-core und künftige gemeinsame UX |

## Dauerhafte Verantwortungsregeln

- Ein Signal hat genau einen Berechnungs-Owner.
- Downstream-Module konsumieren stabile Contracts und detektieren dieselbe
  Rohinformation nicht erneut.
- Policies entscheiden Ziele; Apply-Integrationen führen sie idempotent aus.
- UX ist ersetzbar; langlebige Contracts liegen zwischen Gateway und Frontend.
- Legacy-Entities werden erst nach Consumer-Cutover und Verifikation entfernt.
- Neue Atomics oder Combineds sind keine Zielarchitektur.

## Core-Contracts-Korrektur

Das neue Core-Contracts-Projekt wurde als unabhängige Foundation aus dem
internen Signalgraphen definiert. Es ist keine Kopie und kein stiller
Nachfolger von Core Devices. Der aktuelle verifizierte Slice läuft
read-only und Shadow-only; öffentliche Entities, Services, Actuation und
Policy-Logik sind dort im aktuellen Slice nicht enthalten.

Daher sind folgende Aussagen des älteren Atlas nicht als endgültiger
Zielzustand zu lesen:

- Core Devices sei dauerhaft der einzige Owner jedes künftigen Domain-
  Contracts.
- Opening- und Lock-Contracts müssten unverändert in Core Devices bleiben.
- Ein alter Master- oder Cutover-Ticketstapel könne ohne Neuschnitt
  übernommen werden.

Die fachliche Zielklärung und der Published-Entity-/Consumer-Cutover sind
im aktiven [Core-Contracts-Issue](https://github.com/Levtos/benni-core-contracts/issues/1)
festgehalten.

## Gemeinsame UX-Plattform

Die 19 nativen Backends bleiben bestehen. Die gemeinsame UX besteht aus:

1. statischem Frontend-Bundle mit Shell, Navigation, Designsystem,
   Komponenten und Contract-Modell;
2. dünnem Gateway für Authentifizierung, Normalisierung und Live-Transport.

Verbindlicher Stack: Svelte 5, Vite, TypeScript, Bits UI, kontrolliertes
shadcn-svelte, Tailwind, CSS Custom Properties, Lucide, typisierte Stores und
REST-/WebSocket-Contracts. Details stehen in
[ADR 0001](../../adr/0001-ux-frontend-standard.md).

## Private Betriebsgrenze

Home-Assistant-Instanzen, lokale Konfiguration, private Netzwerkadressen,
MCPHub und LXC 104 sind keine Inhalte dieses öffentlichen Projektgedächtnisses.
Sie werden nur in geschützten Betriebsunterlagen und den dafür vorgesehenen
Issues behandelt.
